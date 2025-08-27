from ast import Num
from typing import Dict, Union, Type
from otree.api import *
from settings import SESSION_CONFIG_DEFAULTS, LANGUAGE_CODE

author = "Nathaniel Lawrence, LEMMA, Université Panthéon-Assas"
doc = """
Presents final results for the session.
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
    """Define constants here, in all-caps"""

    NAME_IN_URL = "session"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_QUESTIONS = 9 + 1
    CONVERSION_FACTOR = SESSION_CONFIG_DEFAULTS["conversion_factor"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# define the questions a player must answer here


class Player(BasePlayer):
    "Register players answers to questions"

    ## choices = [[value,label],[value,label]]
    q1 = models.IntegerField(
        label=Lexicon.session_results_q1,
        choices=[
            [0, Lexicon.session_results_q1_0],
            [1, Lexicon.session_results_q1_1],
            [2, Lexicon.session_results_q1_2],
            [3, Lexicon.session_results_q1_3],
            [4, Lexicon.session_results_q1_4],
            [5, Lexicon.session_results_q1_5],
        ],
    )
    q2 = models.LongStringField(label=Lexicon.session_results_q2, initial="")
    q3 = models.LongStringField(label=Lexicon.session_results_q3, initial="")
    q4 = models.BooleanField(
        label=Lexicon.session_results_q4, choices=[[1, Lexicon.yes], [0, Lexicon.no]]
    )
    q5 = models.BooleanField(
        label=Lexicon.session_results_q5, choices=[[1, Lexicon.yes], [0, Lexicon.no]]
    )
    q6 = models.BooleanField(
        label=Lexicon.session_results_q6, choices=[[1, Lexicon.yes], [0, Lexicon.no]]
    )


def get_behavioral_remuneration(player: Type[Player]) -> float:
    """Calculate remuneration"""
    # Calculate additional remunerations
    behavioral_remuneration = sum(
        v for v in player.participant.remunerated_behavioral.values()
    )
    print("behavioral_remuneration: ", behavioral_remuneration)
    return behavioral_remuneration


def get_behavioral_task_names(player: Type[Player]) -> dict:
    """Create dictionary with language-appropriate task names"""
    task_list = [v for v in player.participant.remunerated_behavioral.keys()]
    task_names = {task: getattr(Lexicon, f"{task}") for task in task_list}
    print(task_names)
    return task_names


def convert_to_euros(amount: float, rounding: int = 2) -> float:
    """Convert to euros for final results table"""
    return round(amount / SESSION_CONFIG_DEFAULTS["conversion_factor"], rounding)


# PAGES
class Final_Results(Page):
    "shows final result of experiment"

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Experiment's final results"""
        participant = player.participant

        # Retrieve and sum each day's Savings Game result
        task_1 = cu(participant.task_results_1)
        # task_2 = cu(participant.task_results_2)
        task_1_euros = convert_to_euros(task_1)
        print("tee type is", type(task_1_euros))
        # task_2_euros = convert_to_euros(task_2)
        remuneration_task = 0
        for i in range(1, SESSION_CONFIG_DEFAULTS["exp_length_rounds"] + 1):
            remuneration_task += getattr(participant, f"task_results_{i}")
        remuneration_task_euros = (
            remuneration_task / SESSION_CONFIG_DEFAULTS["conversion_factor"]
        )

        # Calculate total additional remuneration
        additional_remuneration = float((remuneration_task))

        # Calculate final remuneration
        final_remuneration = float(
            additional_remuneration + SESSION_CONFIG_DEFAULTS["participation_fee"]
        )

        final_remuneration_euros = convert_to_euros(final_remuneration)

        participant.payoff = additional_remuneration  # ! oTree automatically adds the participation fee separately

        return dict(
            task_1=cu(task_1),
            # task_2=cu(task_2),
            task_1_euros=task_1_euros,
            # task_2_euros=task_2_euros,
            remuneration_task=cu(remuneration_task),
            remuneration_task_euros=remuneration_task_euros,
            # behavioral_remuneration=behavioral_remuneration,
            # behavioral_remuneration_euros=behavioral_remuneration_euros,
            final_remuneration=final_remuneration,
            final_remuneration_euros=final_remuneration_euros,
            Lexicon=Lexicon,
            **which_language,
        )


class Feedback(Page):
    "Give feedback after pl yer answered all the questions"

    form_model = "player"
    form_fields = ["q1", "q2", "q3", "q5", "q6", "q4"]

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        return dict(Lexicon=Lexicon, **which_language)


class End(Page):
    "Shows final saving balance after experiment is complete"

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        return dict(Lexicon=Lexicon, **which_language)


class Filler_End(Page):

    @staticmethod
    def is_displayed(player: Type[Player]) -> bool:
        "Displayed if following Intervention 3"
        return player.participant.intervention_3


page_sequence = [Filler_End, Final_Results, Feedback, End]
