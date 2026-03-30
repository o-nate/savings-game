import json
from pprint import pprint  # noqa
from otree.api import *
import random
from settings import (
    SESSION_CONFIG_DEFAULTS,
    SESSION_CONFIGS,
    PARTICIPANT_FIELDS,
    LANGUAGE_CODE,
)

author = "Nathaniel Lawrence, LEMMA, Université Panthéon-Assas"
doc = """
Wisconsin card sorting test: https://doi.org/10.1093/cercor/1.1.62
"""

if LANGUAGE_CODE == "fr":
    from _static.lexicon_fr import Lexicon
else:
    from _static.lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {"en": False, "fr": False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


class C(BaseConstants):
    NAME_IN_URL = "card"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Instructions contants
    # CONVERSION_FACTOR = SESSION_CONFIG_DEFAULTS['conversion_factor']
    CORRECT_ANSWER_FEE = cu(SESSION_CONFIG_DEFAULTS["wisconsin_fee"])
    SWITCH_THRESHOLD = 6
    NUM_TRIALS = 30

    RULES = ["color", "shape", "number"]
    COLORS = ["red", "blue", "green", "yellow"]
    SHAPES = ["circle", "triangle", "star", "plus"]
    NUMBERS = [1, 2, 3, 4]


class Subsession(BaseSubsession):
    matching_rules = models.LongStringField()


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.layout = random_layout()
        p.rule = random.choice(C.RULES)
        p.participant.remunerated_behavioral = {}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # how many they have selected from each deck
    num_trials = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)
    num_correct_in_block = models.IntegerField(initial=0)
    rule = models.StringField(doc="Either color, shape, or number")
    layout = models.StringField()
    is_finished = models.BooleanField(initial=False)

    # Response time
    response_time = models.LongStringField(initial="")


class Trial(ExtraModel):
    player = models.Link(Player)


def random_layout():
    """Randomize order of cards displayed on screen"""
    # color, number, shape, and 0 (which means nothing matches)
    layout = list("cns0")
    random.shuffle(layout)
    return "".join(layout)


def generate_decks(test_card: dict, layout):
    """Shuffle cards in deck"""
    cs = [c for c in C.COLORS if c != test_card["color"]]
    ss = [c for c in C.SHAPES if c != test_card["shape"]]
    ns = [c for c in C.NUMBERS if c != test_card["number"]]
    random.shuffle(cs)
    random.shuffle(ss)
    random.shuffle(ns)

    decks = []
    for letter in layout:
        if letter == "c":
            card = dict(color=test_card["color"], shape=ss.pop(), number=ns.pop())
        elif letter == "s":
            card = dict(shape=test_card["shape"], color=cs.pop(), number=ns.pop())
        elif letter == "n":
            card = dict(number=test_card["number"], shape=ss.pop(), color=cs.pop())
        else:
            card = dict(color=cs.pop(), shape=ss.pop(), number=ns.pop())

        decks.append(card)
    return decks


def live_method(player: Player, data):
    my_id = player.id_in_group
    trial = 1
    if player.is_finished:
        return {my_id: dict(finished=True)}

    resp = {}
    if "deck_number" in data:
        trial += 1
        deck = data["deck_number"]
        # [0] means the first letter of the rule.
        guess = player.layout[deck]
        is_correct = guess == player.rule[0]
        player.num_trials += 1
        player.num_correct += is_correct
        player.num_correct_in_block += is_correct

        if player.num_correct_in_block == C.SWITCH_THRESHOLD:
            other_rules = [r for r in C.RULES if r != player.rule]
            player.rule = random.choice(other_rules)
            player.num_correct_in_block = 0

        # layout changes each turn. otherwise, the user could just keep
        # clicking on the same box for the rest of the block.
        player.layout = random_layout()
        feedback = "🙂" if is_correct else "☹️"

        response_time_base = (
            {} if player.response_time == "" else json.loads(player.response_time)
        )
        response_time_my_list = (
            []
            if not player.num_trials in response_time_base
            else response_time_base[player.num_trials]
        )
        response_time_my_list.append(
            json.dumps(
                {
                    "trial_number": player.num_trials,
                    "guess": guess,
                    "rule": player.rule,
                    "correct": is_correct,
                    "displayed_time": data["displayed_timestamp"],
                    "answered_time": data["answered_timestamp"],
                }
            )
        )
        response_time_base[player.num_trials] = response_time_my_list
        player.response_time = json.dumps(response_time_base)

        resp.update(feedback=feedback)

    test_card = dict(
        color=random.choice(C.COLORS),
        shape=random.choice(C.SHAPES),
        number=random.choice(C.NUMBERS),
    )
    decks = generate_decks(test_card, player.layout)
    resp.update(test_card=test_card, decks=decks)

    if player.num_trials == C.NUM_TRIALS:
        player.is_finished = True
        resp.update(finished=True)

    resp.update(num_trials=player.num_trials)

    return {my_id: resp}


class Intro(Page):
    live_method = live_method

    @staticmethod
    def vars_for_template(player: Player):
        return dict(deck_numbers=range(4), Lexicon=Lexicon, **which_language)


class Play(Page):
    live_method = live_method

    @staticmethod
    def vars_for_template(player: Player):
        return dict(deck_numbers=range(4), Lexicon=Lexicon, **which_language)

    @staticmethod
    def error_message(player: Player, values):
        if not player.is_finished:
            return "Game not finished"


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        reward = player.num_correct * C.CORRECT_ANSWER_FEE
        return dict(
            num_correct=player.num_correct,
            reward=reward,
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        print("Wisconsin num_correct:", player.num_correct)
        player.participant.remunerated_behavioral["wisconsin"] = float(
            player.num_correct * C.CORRECT_ANSWER_FEE
        )


page_sequence = [Intro, Play, Results]
