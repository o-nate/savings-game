import csv
import random

from otree.api import *
from settings import (
    SESSION_CONFIG_DEFAULTS,
    LANGUAGE_CODE,
)

doc = """
Choice list (Holt/Laury, risk preferences, price list, equivalence test, etc)
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
    name_in_url = "h_l"
    players_per_group = None
    num_rounds = 1
    table_template = __name__ + "/table.html"
    lottery_high_a = "2,00 €"
    lottery_low_a = "1,60 €"
    lottery_high_b = "3,85 €"
    lottery_low_b = "0,10 €"
    probability = 50


def read_stimuus_csv():
    """Get probabilities and payoffs for each lottery"""
    f = open(__name__ + "/stimuli.csv", encoding="utf8")
    rows = list(csv.DictReader(f))

    random.shuffle(rows)
    return rows


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        stimuli = read_stimuus_csv()
        for stim in stimuli:
            Trial.create(player=p, **stim)
        p.participant.remunerated_behavioral = {}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ## choices = [[value,label],[value,label]]
    practice = models.IntegerField(widget=widgets.RadioSelect, choices=[[0, 0], [1, 1]])
    raw_responses = models.LongStringField()  # True = chose safe option
    chose_safe = models.BooleanField()
    won_lottery = models.BooleanField()


class Trial(ExtraModel):
    player = models.Link(Player)
    lottery_high_a = models.FloatField()
    lottery_low_a = models.FloatField()
    lottery_high_b = models.FloatField()
    lottery_low_b = models.FloatField()
    probability = models.IntegerField()
    chose_safe = models.BooleanField()
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
        print(responses)
        for trial in trials:
            trial.chose_safe = responses["{} - {}".format(trial.id, trial.probability)]
            print(trial.chose_safe)

        trial = random.choice(trials)
        trial.randomly_chosen = True
        player.chose_safe = trial.chose_safe
        if player.chose_safe:
            player.won_lottery = (trial.probability / 100) > random.random()
            if player.won_lottery:
                payoff = trial.lottery_high_a
            else:
                payoff = trial.lottery_low_a
        else:
            player.won_lottery = (trial.probability / 100) > random.random()
            if player.won_lottery:
                payoff = trial.lottery_high_b
            else:
                payoff = trial.lottery_low_b
        player.payoff = payoff


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        trials = Trial.filter(player=player, randomly_chosen=True)
        return dict(
            trials=trials,
            result=float(player.payoff),
            Lexicon=Lexicon,
            **which_language
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.riskPreferences = (
            float(player.payoff) * SESSION_CONFIG_DEFAULTS["conversion_factor"]
        )
        print("risk preferences payoff: ", player.participant.riskPreferences)
        player.participant.remunerated_behavioral["risk_preferences"] = (
            float(player.payoff) * SESSION_CONFIG_DEFAULTS["conversion_factor"]
        )


page_sequence = [Intro, Intro_2, Stimuli, Results]
