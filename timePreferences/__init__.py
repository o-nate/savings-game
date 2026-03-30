from email.utils import format_datetime
from otree.api import *
from settings import (
    SESSION_CONFIG_DEFAULTS,
    SESSION_CONFIGS,
    PARTICIPANT_FIELDS,
    LANGUAGE_CODE,
)


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


def read_csv_stimuli():
    import csv

    # import random

    f = open(__name__ + "/stimuli.csv", encoding="utf-8-sig")
    rows = [row for row in csv.DictReader(f)]
    # random.shuffle(rows)
    for row in rows:
        # all values in CSV are string unless you convert them
        row["later"] = row["later"]
    return rows


def read_csv_delay():
    import csv
    import random

    f = open(__name__ + "/delay.csv", encoding="utf-8-sig")
    rows = [row for row in csv.DictReader(f)]
    # random.shuffle(rows)
    return rows


def jsonDelay(delayDict):
    import json

    delayJson = json.dumps({"delay": [delay for delay in delayDict]})
    return delayJson


# Define constants here, in all-caps
class C(BaseConstants):
    NAME_IN_URL = "tp"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2

    # Introduction constants
    PAYOUT_1 = 20
    PAYOUT_2 = 100
    INTRO_DELAY = Lexicon.timePreferences_delay_3

    # get larger-later options
    LATER = read_csv_stimuli()

    # get delay
    DELAY = read_csv_delay()
    # DELAY_INDEX = [0,1,2,3,4,5]
    NOW_REWARD = 20
    # DELAY_JSON = jsonDelay(DELAY)
    # print('DELAY_JSON: ', DELAY_JSON)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.participant.remunerated_behavioral = {}


class Group(BaseGroup):
    pass


# define the questions a player must answer here
class Player(BasePlayer):
    ## choices = [[value,label],[value,label],...]

    practice = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[[0, f"{C.PAYOUT_1},00 €"], [1, f"{C.PAYOUT_2},00 €"]],
    )
    delay = models.LongStringField()

    def make_field(number):

        return models.FloatField(
            choices=[
                # Now recorded as 1 to differentiate from 20 in C.LATER
                [1, f"{C.NOW_REWARD},00 €"],
                [C.LATER[number]["later"], f"{C.LATER[number]['later']},00 €"],
            ],
            label="",
            widget=widgets.RadioSelect,
        )

    q1 = make_field(0)
    q2 = make_field(1)
    q3 = make_field(2)
    q4 = make_field(3)
    q5 = make_field(4)
    q6 = make_field(5)
    q7 = make_field(6)
    q8 = make_field(7)
    q9 = make_field(8)
    q10 = make_field(9)


# PAGES
class Intro(Page):
    form_model = "player"
    form_fields = ["practice"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(practice=0)

        error_messages = dict(practice=Lexicon.error_not_correct_selection)

        for field_name, solution in solutions.items():
            if values[field_name] != solution:
                error_messages = error_messages[field_name]
                return error_messages

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Intro_2(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random
        import copy

        new_delay = copy.deepcopy(C.DELAY.copy())
        random.shuffle(new_delay)
        for r in range(1, C.NUM_ROUNDS + 1):
            player.in_round(r).delay = jsonDelay(new_delay)


class TimePreferences(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]
        random.shuffle(form_fields)
        return form_fields

    @staticmethod
    def vars_for_template(player):
        import json

        newer_delay = json.loads(player.delay)
        print(
            "participant:",
            player.participant.id_in_session,
            "new_delay: ",
            newer_delay["delay"][(player.round_number - 1)]["delay"],
        )
        # delay = new_delay[(player.round_number - 1)]['delay']
        return dict(
            delay=getattr(
                Lexicon,
                "timePreferences_delay_%s"
                % newer_delay["delay"][(player.round_number - 1)]["delay"],
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player):
        return dict(
            Lexicon=Lexicon,
            **which_language,
        )


page_sequence = [Intro, Intro_2, TimePreferences, Results]


def custom_export(players):
    yield ["participant_code", "delay"]

    for player in players:
        yield [player.participant.code, player.delay]
