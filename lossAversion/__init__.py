from otree.api import *
from settings import (
    SESSION_CONFIG_DEFAULTS,
    SESSION_CONFIGS,
    PARTICIPANT_FIELDS,
    LANGUAGE_CODE,
)

author = "Nathaniel Lawrence, LEMMA, Université Panthéon-Assas"
doc = """
Based off of Choice List (Holt/Laury, risk preferences, price list, equivalence test, etc)
From: Gerhard Riener, https://www.otreehub.com/projects/morning-beach-6401/
"""

if LANGUAGE_CODE == "fr":
    from _static.lexicon_fr import Lexicon
else:
    from _static.lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {"en": False, "fr": False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


class Constants(BaseConstants):
    name_in_url = "lav"
    players_per_group = None
    num_rounds = 1
    table_template = __name__ + "/table.html"

    # Introduction constants
    WIN = cu(1200)
    LOSE = cu(600)


def read_csv():
    import csv
    import random

    f = open(__name__ + "/stimuli.csv", encoding="utf8")
    rows = list(csv.DictReader(f))

    random.shuffle(rows)
    return rows


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        stimuli = read_csv()
        for stim in stimuli:
            Trial.create(player=p, **stim)
        p.participant.remunerated_behavioral = {}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    practice = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[[0, Lexicon.toss_coin], [1, Lexicon.dont_toss_coin]],
    )
    raw_responses = models.LongStringField()
    chose_toss = models.BooleanField()  # 1 = chose coin toss
    won_toss = models.BooleanField()


class Trial(ExtraModel):
    player = models.Link(Player)
    toss_win = models.CurrencyField()
    toss_lose = models.CurrencyField()
    no_toss_a = models.CurrencyField()
    no_toss_b = models.CurrencyField()
    probability = models.FloatField()
    chose_toss = models.BooleanField()
    randomly_chosen = models.BooleanField(initial=False)


# PAGES
class Intro(Page):
    form_model = "player"
    form_fields = ["practice"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(practice=1)

        error_messages = dict(practice=Lexicon.error_not_correct_selection)

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages = error_messages[field_name]
                return error_messages


class Intro_2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class Stimuli(Page):
    form_model = "player"
    form_fields = ["raw_responses"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            trials=Trial.filter(player=player), Lexicon=Lexicon, **which_language
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import json
        import random

        trials = Trial.filter(player=player)

        responses = json.loads(player.raw_responses)
        for trial in trials:
            trial.chose_toss = responses["{} - {}".format(trial.id, trial.toss_lose)]

        trial = random.choice(trials)
        trial.randomly_chosen = True
        player.chose_toss = trial.chose_toss
        if player.chose_toss:
            player.won_toss = (trial.probability / 100) > random.random()
            if player.won_toss:
                payoff = trial.toss_win
            else:
                payoff = trial.toss_lose * -1
        else:
            if player.field_maybe_none("won_toss"):
                payoff = trial.no_toss_a
            else:
                payoff = trial.no_toss_b
        player.payoff = payoff


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        trials = Trial.filter(player=player, randomly_chosen=True)
        reward = player.payoff
        print(reward)
        return dict(trials=trials, reward=reward, Lexicon=Lexicon, **which_language)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.remunerated_behavioral["loss_aversion"] = float(
            player.payoff
        )


page_sequence = [Intro, Intro_2, Stimuli, Results]
