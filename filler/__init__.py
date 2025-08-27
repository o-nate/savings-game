from typing import Type

from otree.api import *
from settings import LANGUAGE_CODE

author = "Nathaniel Archer Lawrence"
doc = """For debugging and testing:
Use this app to pre-fill any necessary participant_fields to make an app
work as a standalone.
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
    NAME_IN_URL = "filler"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Filler(Page):

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        """Set participant values for demo purposes"""
        player.participant.instructions = "control"
        print("Instructions treatment group:", player.participant.instructions)
        player.participant.intervention = "treatment"
        print("Intervention treatment group:", player.participant.intervention)
        player.participant.round = 1
        print("round:", player.participant.round)
        player.participant.task_results_1 = 1000
        print("task_results_1:", player.participant.task_results_1)
        player.participant.inflation = [1012, 430]
        print("inflation: ", player.participant.inflation)

        ## Set errors for Experiment 2 interventions
        errors_dict = {"early": 1, "late": 1, "excess": 0}
        setattr(player.participant, f"errors_{player.participant.round}", errors_dict)


page_sequence = [Filler]
