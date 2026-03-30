from otree.api import *
from settings import SESSION_CONFIG_DEFAULTS, LANGUAGE_CODE

author = "Nathaniel Lawrence, LEMMA, Université Paris-Panthéon-Assas"
doc = """
This app measures subjects' knowledge of, numeracy related to (i.e. compounding), 
and awareness of inflation.

Certain questions have response time measured as well.
"""
# NOTE:
# In the results, when the response time is recorded as 0, this means the subject
# did not click the next button (i.e. the page timed out due to the timer).

# Sliders provided courtesy of:
# Max R. P. Grossmann, https://gitlab.com/gr0ssmann/otree_slider

# &

# Van Pelt, V. F. J. (2020, February 19). Sliders with feedback and without
# anchoring. Accounting Experiments,
# Available at: https://www.accountingexperiments.com/post/sliders/.


if LANGUAGE_CODE == "fr":
    from _static.lexicon_fr import Lexicon
else:
    from _static.lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {"en": False, "fr": False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


# Define constants here, in all-caps
class C(BaseConstants):
    NAME_IN_URL = "pda"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_PAGES = 11
    TIME_LIMIT = SESSION_CONFIG_DEFAULTS["time_limit"]
    # SLIDER_TEST = -73
    QUESTION_PRICE = 1000
    CHANGES = [[1, Lexicon.increase], [0, Lexicon.no_change], [-1, Lexicon.decrease]]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ## choices = [[value,label],[value,label]]

    # Level of knowledge of previous inflation rates (Macchia et al., 2018)
    infK_highest = models.FloatField(label=Lexicon.infK_highest, min=-1000, max=1000)
    infK_lowest = models.FloatField(label=Lexicon.infK_lowest, min=-1000, max=1000)
    infK_12 = models.FloatField(label=Lexicon.infK_12, min=-1000, max=1000)
    infK_future = models.FloatField(label=Lexicon.infK_future, min=-1000, max=1000)

    # Level of knowledge of calculation of impact of compound interest (Macchia et al., 2018)
    infCI_1 = models.FloatField(
        label=Lexicon.infCI_1.format(C.QUESTION_PRICE), min=0, max=9999
    )
    responseTime_CI1 = models.FloatField(initial=0)

    infCI_2 = models.FloatField(
        label=Lexicon.infCI_2.format(C.QUESTION_PRICE), widget=widgets.RadioSelect
    )
    responseTime_CI2 = models.FloatField(initial=0)

    infCI_3 = models.FloatField(
        label=Lexicon.infCI_3.format(C.QUESTION_PRICE), widget=widgets.RadioSelect
    )
    responseTime_CI3 = models.FloatField(initial=0)

    infCI_4 = models.FloatField(
        label=Lexicon.infCI_4.format(C.QUESTION_PRICE), min=0, max=999999
    )
    responseTime_CI4 = models.FloatField(initial=0)

    # Inflation Awareness
    inf_4 = models.IntegerField(
        choices=[
            [1, Lexicon.increased],
            [-1, Lexicon.decreased],
            [0, Lexicon.stayed_same],
            [5, Lexicon.not_applicable],
            [9, Lexicon.I_do_not_know],
        ],
        label=Lexicon.inf_4,
        widget=widgets.RadioSelect,
    )
    inf_5 = models.IntegerField(
        choices=[
            [1, Lexicon.increased],
            [-1, Lexicon.decreased],
            [0, Lexicon.stayed_same],
            [5, Lexicon.not_applicable],
            [9, Lexicon.I_do_not_know],
        ],
        label=Lexicon.inf_5,
        widget=widgets.RadioSelect,
    )
    inf_5_change = models.FloatField(min=0, max=500)
    inf_7 = models.IntegerField(
        choices=[
            [1, Lexicon.increase],
            [-1, Lexicon.decrease],
            [0, Lexicon.stay_same],
            [5, Lexicon.not_applicable],
            [9, Lexicon.I_do_not_know],
        ],
        label=Lexicon.inf_7,
        widget=widgets.RadioSelect,
    )
    inf_7_change = models.FloatField(min=0, max=500)

    ## Inflation adjustment
    inf_food = models.IntegerField(
        choices=C.CHANGES,
        label=Lexicon.inf_food,
        widget=widgets.RadioSelect,
    )
    inf_food_change = models.FloatField(min=0, max=500)
    inf_housing = models.IntegerField(
        choices=C.CHANGES,
        label=Lexicon.inf_housing,
        widget=widgets.RadioSelect,
    )
    inf_housing_change = models.FloatField(min=0, max=500)
    inf_other = models.IntegerField(
        choices=C.CHANGES,
        label=Lexicon.inf_other,
        widget=widgets.RadioSelect,
    )
    inf_other_change = models.FloatField(min=0, max=500)
    inf_quantity = models.IntegerField(
        choices=C.CHANGES,
        label=Lexicon.inf_quantity,
        widget=widgets.RadioSelect,
    )
    inf_quantity_change = models.FloatField(min=0, max=500)
    inf_stock = models.IntegerField(
        choices=C.CHANGES,
        label=Lexicon.inf_stock,
        widget=widgets.RadioSelect,
    )
    inf_stock_change = models.FloatField(min=0, max=500)
    inf_checking = models.IntegerField(
        choices=C.CHANGES,
        label=Lexicon.inf_checking,
        widget=widgets.RadioSelect,
    )
    inf_checking_change = models.FloatField(min=0, max=500)
    inf_savings = models.IntegerField(
        choices=C.CHANGES,
        label=Lexicon.inf_savings,
        widget=widgets.RadioSelect,
    )
    inf_savings_change = models.FloatField(min=0, max=500)


# FUNCTIONS
# Choice randomization
def infCI_2_choices(player):
    import random

    choices = [
        [1, "{} €".format(C.QUESTION_PRICE * 2)],
        [2, Lexicon.inf_more_than.format(C.QUESTION_PRICE * 2)],
        [3, Lexicon.inf_less_than.format(C.QUESTION_PRICE * 2)],
    ]
    random.shuffle(choices)
    return choices


def infCI_3_choices(player):
    import random

    choices = [
        [1, "{} €".format(C.QUESTION_PRICE + 150)],
        [2, Lexicon.inf_more_than.format(C.QUESTION_PRICE + 150)],
        [3, Lexicon.inf_less_than.format(C.QUESTION_PRICE + 150)],
    ]
    random.shuffle(choices)
    return choices


def determine_form_fields(player: Player, questions: list) -> list:
    """Identify which follow-up questions to include"""
    follow_ups = []
    # participant = player.participant
    for q in questions:
        if getattr(player, q) != 0:
            follow_ups.append(f"{q}_change")
    return follow_ups


def get_rt_field(questions: list) -> str:
    """Get response time form_field"""
    return questions[-1]


def determine_change(player: Player, questions: list) -> dict:
    """For each percentage change question, determine if asking about an increase or decrease"""
    follow_ups = {}
    for q in questions:
        response = getattr(player, q)
        if response != 0:
            follow_ups[f"{q}_change"] = Lexicon.inf_change[q][response]
    return follow_ups


# PAGES
class Instructions(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class IK_1(Page):
    form_model = "player"
    form_fields = [
        "infK_highest",
        "infK_lowest",
        "infK_12",
        "infK_future",
    ]
    timeout_seconds = C.TIME_LIMIT

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                0 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class I_TimerStart(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class IN_1(Page):
    form_model = "player"
    form_fields = ["infCI_1", "responseTime_CI1"]

    @staticmethod
    def js_vars(player: Player):
        """Send response time form_field to timer script in HTML"""
        rt_question = get_rt_field(IN_1.form_fields)
        return dict(timed_question=rt_question)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                1 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class IN_2(Page):
    form_model = "player"
    form_fields = ["infCI_2", "responseTime_CI2"]

    @staticmethod
    def js_vars(player: Player):
        """Send response time form_field to timer script in HTML"""
        print(Page.form_fields)
        rt_question = get_rt_field(IN_2.form_fields)
        return dict(timed_question=rt_question)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                2 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class IN_3(Page):
    form_model = "player"
    form_fields = ["infCI_3", "responseTime_CI3"]

    @staticmethod
    def js_vars(player: Player):
        """Send response time form_field to timer script in HTML"""
        print(Page.form_fields)
        rt_question = get_rt_field(IN_3.form_fields)
        print(rt_question)
        return dict(timed_question=rt_question)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                3 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class IN_4(Page):
    form_model = "player"
    form_fields = ["infCI_4", "responseTime_CI4"]

    @staticmethod
    def js_vars(player: Player):
        """Send response time form_field to timer script in HTML"""
        print(Page.form_fields)
        rt_question = get_rt_field(IN_4.form_fields)
        print(rt_question)
        return dict(timed_question=rt_question)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                4 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class I_TimerEnd(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class IA_1(Page):
    form_model = "player"
    form_fields = ["inf_4", "inf_5"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                5 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class IA_2(Page):
    form_model = "player"
    form_fields = ["inf_5_change"]

    @staticmethod
    def js_vars(player: Player):
        """Send follow up questions with increase or decrease specified"""
        follow_up_qs = determine_change(player, ["inf_5"])
        questions = determine_form_fields(player, ["inf_5"])
        return dict(follow_up_qs=follow_up_qs, fields=questions)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                6 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def is_displayed(player):
        return player.inf_5 == 1 or player.inf_5 == -1


class IA_3(Page):
    form_model = "player"
    form_fields = ["inf_7"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                7 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class IA_4(Page):
    form_model = "player"
    form_fields = ["inf_7_change"]

    @staticmethod
    def js_vars(player: Player):
        """Send follow up questions with increase or decrease specified"""
        follow_up_qs = determine_change(player, ["inf_7"])
        questions = determine_form_fields(player, ["inf_7"])
        return dict(follow_up_qs=follow_up_qs, fields=questions)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                8 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def is_displayed(player):
        return player.inf_7 == 1 or player.inf_7 == -1


class IA_5(Page):
    form_model = "player"
    form_fields = [
        "inf_food",
        "inf_housing",
        "inf_other",
        "inf_quantity",
        "inf_stock",
        "inf_checking",
        "inf_savings",
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                9 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class IA_6(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        """Add form_fields based on responses in IA_5"""
        return determine_form_fields(player, IA_5.form_fields)

    @staticmethod
    def is_displayed(player: Player):
        """Displays page if at least one question on previous was answered as
        having had a change"""
        return len(determine_form_fields(player, IA_5.form_fields)) >= 1

    @staticmethod
    def js_vars(player: Player):
        """Send follow up questions with increase or decrease specified"""
        follow_up_qs = determine_change(player, IA_5.form_fields)
        questions = determine_form_fields(player, IA_5.form_fields)
        return dict(follow_up_qs=follow_up_qs, fields=questions)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                10 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class Results(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                C.NUM_PAGES / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


page_sequence = [
    Instructions,
    I_TimerStart,
    IK_1,
    I_TimerEnd,
    IN_1,
    IN_2,
    IN_3,
    IN_4,
    IA_1,
    IA_2,
    IA_3,
    IA_4,
    IA_5,
    IA_6,
    Results,
]
