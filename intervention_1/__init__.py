from decimal import *
import random

from otree.api import *

from settings import SESSION_CONFIG_DEFAULTS, PARTICIPANT_FIELDS, LANGUAGE_CODE

author = "Nathaniel Archer Lawrence, LEMMA, Université Panthéon-Assas - Paris II"
doc = """
Savings Game intervention: Performance feedback and reflection question(s)
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
    NAME_IN_URL = "task_int"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_PAGES = 9

    MAX_PERFORMANCE = {"430": 4119.28, "1012": 2420.94}
    INTEREST_RATE = SESSION_CONFIG_DEFAULTS["interest_rate"] * 100
    PRICE_1 = 12
    PRICE_2 = 12.12

    ERROR_Q_CHOICES = [
        [3, Lexicon.yes],
        [2, Lexicon.no],
        [0, Lexicon.maybe],
    ]

    ERROR_Q_CHOICES_NO_ERROR = [
        [2, Lexicon.yes],
        [3, Lexicon.no],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ## choices = [[value, label],[value, label],...]
    intro_1 = models.IntegerField(label="", widget=widgets.RadioSelect)
    # Counts number of attempts for question
    intro_1_errors = models.IntegerField(initial=0, blank=True)
    q_early = models.IntegerField(label="", widget=widgets.RadioSelect)
    confirm_early = models.IntegerField(
        label="",
        widget=widgets.RadioSelect,
    )
    q_late = models.IntegerField(label="", widget=widgets.RadioSelect)
    confirm_late = models.IntegerField(
        label="",
        widget=widgets.RadioSelect,
    )
    q_excess = models.IntegerField(label="", widget=widgets.RadioSelect)
    confirm_excess = models.IntegerField(
        label="",
        widget=widgets.RadioSelect,
    )


def intro_1_choices(player):
    """Randomize order of choices"""
    choices = [
        [1, Lexicon.task_int_high_inf],
        [0, Lexicon.task_int_low_inf],
    ]
    random.shuffle(choices)
    return choices


def q_early_choices(player):
    """Randomize order of choices"""
    choices = C.ERROR_Q_CHOICES.copy()
    random.shuffle(choices)
    return choices


def q_late_choices(player):
    """Randomize order of choices"""
    choices = C.ERROR_Q_CHOICES.copy()
    random.shuffle(choices)
    return choices


def q_excess_choices(player):
    """Randomize order of choices"""
    choices = C.ERROR_Q_CHOICES.copy()
    random.shuffle(choices)
    return choices


def confirm_early_choices(player):
    """Adjust validation per errors committed"""
    participant = player.participant
    current_round = participant.round
    errors = getattr(participant, f"errors_{current_round}")["early"]
    if errors > 0:
        choices = C.ERROR_Q_CHOICES[0:2].copy()
    else:
        choices = C.ERROR_Q_CHOICES_NO_ERROR
    return choices


def confirm_late_choices(player):
    """Adjust validation per errors committed"""
    participant = player.participant
    current_round = participant.round
    errors = getattr(participant, f"errors_{current_round}")["late"]
    if errors > 0:
        choices = C.ERROR_Q_CHOICES[0:2].copy()
    else:
        choices = C.ERROR_Q_CHOICES_NO_ERROR
    return choices


def confirm_excess_choices(player):
    """Adjust validation per errors committed"""
    participant = player.participant
    current_round = participant.round
    errors = getattr(participant, f"errors_{current_round}")["excess"]
    if errors > 0:
        choices = C.ERROR_Q_CHOICES[0:2].copy()
    else:
        choices = C.ERROR_Q_CHOICES_NO_ERROR
    return choices


def determine_error(player, error):
    """Determine whether given error was committed"""
    participant = player.participant
    current_round = participant.round
    errors = getattr(participant, f"errors_{current_round}")[error]
    if errors > 0:
        explanations = {3: "true", 2: "false", 0: "true"}
    else:
        explanations = {3: "false", 2: "true", 0: "false"}
    return explanations


# PAGES
class Int_1(Page):

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]
        percent_max = performance / max_performance * 100
        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            percent_max=percent_max,
            Lexicon=Lexicon,
            **which_language,
        )


class Int_2(Page):
    form_model = "player"

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]
        opportunity_cost = max_performance - performance
        ## Retrieve stock to determine errors commmitted during game (early, late, excess)
        current_round = participant.round
        inflation = participant.inflation[current_round - 1]
        before = 3 if inflation == 1012 else 30
        after = before + 3
        end = C.NUM_ROUNDS
        errors_ = [
            f"errors_{current_round}",
            f"errors_{current_round}",
            f"errors_{current_round}",
        ]
        ## Save finalStock at each benchmark month
        for field, amount in zip(errors_, [before, after, end]):
            print(amount, getattr(participant, field))
        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            opportunity_cost=cu(opportunity_cost),
            # For progress bars
            percentage=round(
                1 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            Lexicon=Lexicon,
            **which_language,
        )


class Int_3(Page):
    form_model = "player"
    form_fields = ["intro_1", "intro_1_errors"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            # For progress bars
            percentage=round(
                2 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE), 2),
            price_1=cu(C.PRICE_1),
            price_2=cu(C.PRICE_2),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(intro_1=0)
        error_messages = dict(
            intro_1=Lexicon.error_task_int_intro_1.format(
                cu(C.PRICE_2),
                cu(C.PRICE_1),
                cu(C.PRICE_1),
                round((C.PRICE_2 - C.PRICE_1) / C.PRICE_1 * 100, 1),
                round(C.INTEREST_RATE, 1),
            )
        )
        for field_name, solution in solutions.items():
            if values[field_name] != solution:
                error_messages = error_messages[field_name]
                setattr(
                    player,
                    f"{field_name}_errors",
                    getattr(player, f"{field_name}_errors") + 1,
                )
                print(f"{field_name}_errors: ", getattr(player, f"{field_name}_errors"))
                return error_messages


class Int_4(Page):
    form_model = "player"
    form_fields = ["q_early"]

    @staticmethod
    def js_vars(player):
        """Send explanations based on whether error was committed"""
        answer_options = determine_error(player, "early")
        return dict(
            cost_type="early",
            explanations=Lexicon.task_int_explain["early"],
            answer_options=answer_options,
        )

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]

        ## Retrieve stock to determine errors commmitted during game (early, late, excess)
        current_round = participant.round
        inflation = participant.inflation[current_round - 1]

        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            # For progress bars
            percentage=round(
                3 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            Lexicon=Lexicon,
            **which_language,
        )


class Int_4_b(Page):
    form_model = "player"
    form_fields = ["confirm_early"]

    @staticmethod
    def js_vars(player):
        """Send explanations based on whether error was committed"""
        answer_options = determine_error(player, "early")
        return dict(
            cost_type="early",
            response=player.q_early,
            explanations=Lexicon.task_int_explain["early"],
            answer_options=answer_options,
        )

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]

        ## Retrieve stock to determine errors commmitted during game (early, late, excess)
        current_round = participant.round
        inflation = participant.inflation[current_round - 1]

        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            # For progress bars
            percentage=round(
                4 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            Lexicon=Lexicon,
            **which_language,
        )


class Int_5(Page):
    form_model = "player"
    form_fields = ["q_late"]

    @staticmethod
    def js_vars(player):
        """Send explanations based on whether error was committed"""
        answer_options = determine_error(player, "late")
        return dict(
            cost_type="late",
            explanations=Lexicon.task_int_explain["late"],
            answer_options=answer_options,
        )

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]

        ## Retrieve stock to determine errors commmitted during game (early, late, excess)
        current_round = participant.round
        inflation = participant.inflation[current_round - 1]

        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            # For progress bars
            percentage=round(
                5 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            Lexicon=Lexicon,
            **which_language,
        )


class Int_5_b(Page):
    form_model = "player"
    form_fields = ["confirm_late"]

    @staticmethod
    def js_vars(player):
        """Send explanations based on whether error was committed"""
        answer_options = determine_error(player, "late")
        return dict(
            cost_type="late",
            response=player.q_late,
            explanations=Lexicon.task_int_explain["late"],
            answer_options=answer_options,
        )

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]

        ## Retrieve stock to determine errors commmitted during game (early, late, excess)
        current_round = participant.round
        inflation = participant.inflation[current_round - 1]

        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            # For progress bars
            percentage=round(
                6 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            Lexicon=Lexicon,
            **which_language,
        )


class Int_6(Page):
    form_model = "player"
    form_fields = ["q_excess"]

    @staticmethod
    def js_vars(player):
        """Send explanations based on whether error was committed"""
        answer_options = determine_error(player, "excess")
        return dict(
            cost_type="excess",
            explanations=Lexicon.task_int_explain["excess"],
            answer_options=answer_options,
        )

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]

        ## Retrieve stock to determine errors commmitted during game (early, late, excess)
        current_round = participant.round
        inflation = participant.inflation[current_round - 1]

        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            # For progress bars
            percentage=round(
                7 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            Lexicon=Lexicon,
            **which_language,
        )


class Int_6_b(Page):
    form_model = "player"
    form_fields = ["confirm_excess"]

    @staticmethod
    def js_vars(player):
        """Send explanations based on whether error was committed"""
        answer_options = determine_error(player, "excess")
        return dict(
            cost_type="excess",
            response=player.q_excess,
            explanations=Lexicon.task_int_explain["excess"],
            answer_options=answer_options,
        )

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        performance = getattr(
            participant, f"task_results_{participant.round}", float(0)
        )
        inflation = getattr(participant, "inflation")[participant.round - 1]
        max_performance = C.MAX_PERFORMANCE[str(inflation)]

        ## Retrieve stock to determine errors commmitted during game (early, late, excess)
        current_round = participant.round
        inflation = participant.inflation[current_round - 1]

        return dict(
            performance=cu(performance),
            max_performance=cu(max_performance),
            # For progress bars
            percentage=round(
                8 / C.NUM_PAGES * 100,
            ),
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            Lexicon=Lexicon,
            **which_language,
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
            **which_language,
        )


page_sequence = [
    Int_1,
    Int_2,
    Int_3,
    Int_4,
    Int_4_b,
    Int_5,
    Int_5_b,
    Int_6,
    Int_6_b,
    Results,
]
