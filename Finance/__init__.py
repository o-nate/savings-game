from otree.api import *
from settings import SESSION_CONFIG_DEFAULTS, LANGUAGE_CODE

author = "Nathaniel Lawrence, LEMMA, Université Panthéon-Assas"
doc = """
This app provides a consumption simultion app, combined with surveys on demographics; financial knowledge, behavior, and attitude; and numeracy;
as well as tests of time preferences and compulsivity/learning rates. 
"""

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
    NAME_IN_URL = "fl"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_PAGES = 3
    CONVERSION_FACTOR = SESSION_CONFIG_DEFAULTS["conversion_factor"]
    CORRECT_ANSWER_FEE = cu(
        SESSION_CONFIG_DEFAULTS["correct_answer_fee"] * CONVERSION_FACTOR
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# define the questions a player must answer here


class Player(BasePlayer):

    ### choices = [[value,label],[value,label],...]

    # Financial Knowledge

    finK_1 = models.IntegerField(
        choices=[
            [-1, Lexicon.finK_1_choice_1],
            [0, Lexicon.finK_1_choice_2],
            [1, Lexicon.finK_1_choice_3],
            [9, Lexicon.I_do_not_know],
        ],
        label=Lexicon.finK_1,
        widget=widgets.RadioSelect,
    )
    # Response time
    responseTime_1 = models.FloatField(initial=0)

    finK_2 = models.IntegerField(
        choices=[
            [
                1,
                Lexicon.finK_2_choice_1,
            ],
            [0, Lexicon.finK_2_choice_2],
            [-1, Lexicon.finK_2_choice_3],
            [9, Lexicon.I_do_not_know],
        ],
        label=Lexicon.finK_2,
        widget=widgets.RadioSelect,
    )
    responseTime_2 = models.FloatField(initial=0)

    finK_9 = models.BooleanField(
        choices=[[True, Lexicon.true], [False, Lexicon.false]],
        label=Lexicon.finK_9,
        widget=widgets.RadioSelect,
    )
    responseTime_9 = models.FloatField(initial=0)


# PAGES
class FIntro(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class FK_1(Page):
    form_model = "player"
    form_fields = ["finK_1", "responseTime_1"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            # For progress bars
            percentage=round(
                0 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language
        )


class FK_1b(Page):
    form_model = "player"
    form_fields = ["finK_2", "responseTime_2"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            # For progress bars
            percentage=round(
                1 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language
        )


class FK_3c(Page):
    form_model = "player"
    form_fields = ["finK_9", "responseTime_9"]

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                2 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language
        )


class Results(Page):

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                C.NUM_PAGES / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language
        )


page_sequence = [
    FIntro,
    FK_1,
    FK_1b,
    FK_3c,
    Results,
]
