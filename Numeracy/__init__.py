from ast import Num
from otree.api import *
from settings import (
    SESSION_CONFIG_DEFAULTS,
    SESSION_CONFIGS,
    PARTICIPANT_FIELDS,
    LANGUAGE_CODE,
)

author = "Nathaniel Lawrence, LEMMA, Université Panthéon-Assas"
doc = """
Berlin Numeracy Test
From: Cokely, E. T., Galesic, M., Schulz, E., Ghazal, S., & Garcia-Retamero, R. (2012).
Measuring risk literacy: The berlin numeracy test. Judgment and Decision Making, 7(1), 25–47. 
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
    NAME_IN_URL = "bnt"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_PAGES = 4
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
    # Numeracy
    num_1 = models.IntegerField(label=Lexicon.num_1, min=0)
    num_2a = models.IntegerField(label=Lexicon.num_2a, min=0)
    num_2b = models.IntegerField(label=Lexicon.num_2b, min=0)
    num_3 = models.IntegerField(label=Lexicon.num_3, min=0)
    # Response time
    responseTime_1 = models.FloatField(initial=0)
    responseTime_2a = models.FloatField(initial=0)
    responseTime_2b = models.FloatField(initial=0)
    responseTime_3 = models.FloatField(initial=0)

    # Numeracy Attitude
    numatt_1 = models.StringField(
        choices=[
            [1, "1 - {}".format(Lexicon.numatt_not_confident)],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5 - {}".format(Lexicon.numatt_confident)],
        ],
        label=Lexicon.numatt_1,
        widget=widgets.RadioSelect,
    )
    numatt_2 = models.StringField(
        choices=[
            [1, "1 - {}".format(Lexicon.numatt_not_confident)],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5 - {}".format(Lexicon.numatt_confident)],
        ],
        label=Lexicon.numatt_2,
        widget=widgets.RadioSelect,
    )
    numatt_3 = models.StringField(
        choices=[
            [1, "1 - {}".format(Lexicon.numatt_not_confident)],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5 - {}".format(Lexicon.numatt_confident)],
        ],
        label=Lexicon.numatt_3,
        widget=widgets.RadioSelect,
    )
    numatt_4 = models.StringField(
        choices=[
            [1, "1 - {}".format(Lexicon.numatt_not_confident)],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5 - {}".format(Lexicon.numatt_confident)],
        ],
        label=Lexicon.numatt_4,
        widget=widgets.RadioSelect,
    )


# FUNCTIONS


# PAGES
class BNT_Intro(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class BNT_1(Page):
    form_model = "player"
    form_fields = ["num_1", "responseTime_1"]

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                0 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language
        )


class BNT_2a(Page):
    form_model = "player"
    form_fields = ["num_2a", "responseTime_2a"]

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                1 / (C.NUM_PAGES - 1) * 100,
            ),
            Lexicon=Lexicon,
            **which_language
        )

    @staticmethod
    def is_displayed(player):
        return player.num_1 != 25


class BNT_2b(Page):
    form_model = "player"
    form_fields = ["num_2b", "responseTime_2b"]

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                1 / C.NUM_PAGES * 100,
            ),
            Lexicon=Lexicon,
            **which_language
        )

    @staticmethod
    def is_displayed(player):
        return player.num_1 == 25


class BNT_3(Page):
    form_model = "player"
    form_fields = ["num_3", "responseTime_3"]

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

    @staticmethod
    def is_displayed(player):
        if player.field_maybe_none("num_2a") is None:
            if player.num_2b != 20:
                return True


class NAtt(Page):
    form_model = "player"
    form_fields = ["numatt_1", "numatt_2", "numatt_3", "numatt_4"]

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        if player.field_maybe_none("num_2a"):
            percentage = 0.67
        elif player.field_maybe_none("num_2b") == 20:
            percentage = 0.5
        else:
            percentage = 0.75

        return dict(
            percentage=round(percentage * 100), Lexicon=Lexicon, **which_language
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


page_sequence = [BNT_Intro, BNT_1, BNT_2a, BNT_2b, BNT_3, NAtt, Results]
