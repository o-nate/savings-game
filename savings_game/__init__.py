"""Defines data collected and functions for the Savings Game"""

import csv
from typing import Any, Generator, List, Dict, Union, Type
from decimal import *
import json
import random
from re import sub
import statistics

from otree.api import *

from settings import SESSION_CONFIG_DEFAULTS, LANGUAGE_CODE

author = "Nathaniel Archer Lawrence"
doc = """
The Savings Game: Inflation simulation to measure savings and consumption
decision making
"""

if LANGUAGE_CODE == "fr":
    from _static.lexicon_fr import Lexicon
else:
    from _static.lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {"en": False, "fr": False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


def read_csv_catalog() -> List[Dict[str, Union[str, float]]]:
    """Convert csv with product catalog to dict"""
    with open(__name__ + "/catalog.csv", encoding="utf-8-sig") as file:
        f = file
        rows = [row for row in csv.DictReader(f)]
        for row in rows:
            # Convert values in CSV from string to float
            row["unit_price"] = float(row["unit_price"])
            # Translate name of good
            row["name"] = Lexicon.food
        return rows


def read_csv_inflation() -> List[Dict[str, Union[str, float]]]:
    """Convert csv with inflation to dict"""
    with open(__name__ + "/animal_spirits.csv", encoding="utf-8-sig") as file:
        f = file
        rows = [row for row in csv.DictReader(f)]
        for row in rows:
            # all values in CSV are string unless you convert them
            # / 12 # convert from the annualized rate
            row["430"] = float(row["430"])
            # / 12 # convert from the annualized rate
            row["1012"] = float(row["1012"])
            row["period"] = int(row["period"])
        return rows


class C(BaseConstants):
    """Experimenter-defined constants, see SESSION_CONFIG_DEFAULTS for
    additional experiment-wide constants that may be used here."""

    NAME_IN_URL = "task"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = SESSION_CONFIG_DEFAULTS["task_duration"]
    TIME_LIMIT = SESSION_CONFIG_DEFAULTS["time_limit"]

    # Consumption constants
    INITIAL_ENDOWMENT = SESSION_CONFIG_DEFAULTS["initial_endowment"]
    INCOME = SESSION_CONFIG_DEFAULTS["income"]
    INTEREST_RATE = SESSION_CONFIG_DEFAULTS["interest_rate"]
    CONSUMPTION_RATE = 1  # Amount of good consumed from stock balance each period
    MONETARY_POLICY = SESSION_CONFIG_DEFAULTS["monetary_policy"]

    # Define window for calculating late stock
    LATE_WINDOW = 3

    # Inflation parameters from csv
    INFLATION = read_csv_inflation()
    # period = ID in dict
    INFLATION_DICT = {row["period"]: row for row in INFLATION}

    # List of products taken from csv file
    PRODUCTS = read_csv_catalog()
    # SKU = 'stock keeping unit' = product ID
    PRODUCTS_DICT = {row["sku"]: row for row in PRODUCTS}


class Subsession(BaseSubsession):
    """Subsession not required for the standard Savings Game"""

    pass


class Group(BaseGroup):
    """Group not required for the standard Savings Game"""

    pass


class Player(BasePlayer):
    """Data collected on each subject's (i.e. Player's) performance.
    Each field represents a column in the data table."""

    total_price = models.CurrencyField(initial=0)
    initial_savings = models.CurrencyField(initial=0)
    cash_on_hand = models.CurrencyField(initial=0)
    final_savings = models.CurrencyField(initial=0)
    final_stock = models.IntegerField(initial=0)
    interest_earned = models.CurrencyField(initial=0)
    decision = models.LongStringField(initial="")
    new_price = models.FloatField(initial=C.PRODUCTS_DICT["1"]["unit_price"])
    real_interest = models.FloatField()

    # Response time
    response_time = models.FloatField(initial=0)

    # Inflation estimates
    qualitative_estimate = models.IntegerField(
        label=Lexicon.qualitative_estimate,
        choices=[
            [3, Lexicon.qualitative_est_rapid],
            [2, Lexicon.qualitative_est_moderate],
            [1, Lexicon.qualitative_est_slight],
            [0, Lexicon.qualitative_est_same],
            [-1, Lexicon.qualitative_est_decrease],
        ],
        widget=widgets.RadioSelect,
    )
    qualitative_expectation = models.IntegerField(
        label="",
        choices=[
            [3, Lexicon.qualitative_exp_rapid],
            [2, Lexicon.qualitative_exp_moderate],
            [1, Lexicon.qualitative_exp_slight],
            [0, Lexicon.qualitative_exp_same],
            [-1, Lexicon.qualitative_exp_decrease],
        ],
        widget=widgets.RadioSelect,
    )
    inf_estimate = models.FloatField(
        label=Lexicon.inf_estimate, blank=True, min=-100, max=100
    )
    inf_expectation = models.FloatField(
        label=Lexicon.inf_expectation, blank=True, min=-100, max=100
    )


class Item(ExtraModel):
    """Custom class to create product object and track its price and consumption"""

    player = models.Link(Player)
    sku = models.StringField()
    name = models.StringField()
    quantity = models.IntegerField()
    unit_price = models.CurrencyField()
    new_price = models.FloatField()


def custom_export(players: Type[Player]) -> Generator[Any, Any, Any]:
    """Export Item table"""

    yield [
        "session",
        "participant",
        "round_number",
        "sku",
        "name",
        "quantity",
        "unit_price",
        "new_price",
    ]

    # 'filter' without any args returns everything
    items = Item.filter()
    for item in items:
        player = item.player
        participant = player.participant
        sku = item.sku
        name = item.name
        quantity = item.quantity
        unit_price = item.unit_price
        new_price = item.new_price
        session = player.session
        yield [
            session.code,
            participant.code,
            player.round_number,
            sku,
            name,
            quantity,
            unit_price,
            new_price,
        ]


def qualitative_expectation_choices(
    player: Type[Player],
) -> List[List[Union[int, str]]]:
    """Change answer options for Month 1 versus others"""
    if player.round_number == 1:
        choices = [
            [3, Lexicon.qualitative_exp_rapid_month_1],
            [2, Lexicon.qualitative_exp_moderate_month_1],
            [1, Lexicon.qualitative_exp_slight_month_1],
            [0, Lexicon.qualitative_exp_same_month_1],
            [-1, Lexicon.qualitative_exp_decrease_month_1],
        ]
    else:
        choices = [
            [3, Lexicon.qualitative_exp_rapid],
            [2, Lexicon.qualitative_exp_moderate],
            [1, Lexicon.qualitative_exp_slight],
            [0, Lexicon.qualitative_exp_same],
            [-1, Lexicon.qualitative_exp_decrease],
        ]
    return choices


def calculate_price(player: Player) -> float:
    """Calculate new price of good based on inflation and round in Savings Game"""
    # * Calculate new price
    if player.round_number == 1:
        # * If first month, use original price from C.PRODUCTS_DICT["1"]["unit_price"]
        return float(
            C.PRODUCTS_DICT["1"]["unit_price"]
            * (
                1
                + C.INFLATION_DICT[player.round_number][
                    str(player.participant.inflation[(player.participant.round - 1)])
                ]
            )
        )
    # * If after first month, use price from previous month
    return player.in_round(player.round_number - 1).new_price * (
        1
        + C.INFLATION_DICT[player.round_number][
            str(player.participant.inflation[(player.participant.round - 1)])
        ]
    )


def change_quantity_in_cart(
    player: Type[Player], data_from_click: Dict[str, Union[str, int]]
) -> None:
    """
    Adjust quantity in shopping cart based on the button clicked (+1 or -1) and
    whether or not the item is already in the shopping cart
    """
    # * Add and remove from shopping cart
    if "sku" in data_from_click:
        # * If buttons +1 or -1 clicked to adjust quantity in shopping cart, determine ...
        print("data_from_click", data_from_click)
        # * ... which product
        sku = data_from_click["sku"]
        # * ... if added or removed from cart
        delta = data_from_click["delta"]
        matches = Item.filter(player=player, sku=sku)
        print("matches", matches)
        # * If quantity already in cart ...
        if matches:
            # * ... adjust quantity based on button clicked (+1 or -1)
            [item] = matches
            print("item.quantity", item.quantity)
            item.quantity += delta
            # * If last quantity in cart, remove item from cart
            if item.quantity <= 0:
                item.delete()
        # * If not already in cart, create new item in cart
        else:
            Item.create(
                player=player,
                quantity=delta,
                sku=sku,
                name=C.PRODUCTS_DICT[sku]["name"],
                unit_price=player.new_price,
            )


def calculate_initial_savings(player: Player) -> float:
    """Calculate savings held at beginning of new period"""
    if player.round_number == 1:
        return C.INITIAL_ENDOWMENT
    return player.in_round(player.round_number - 1).final_savings * (
        1
        + (
            C.INTEREST_RATE
            + (
                C.MONETARY_POLICY
                * C.INFLATION_DICT[player.round_number - 1][
                    str(player.participant.inflation[(player.participant.round - 1)])
                ]
            )
        )
    )


def calculate_final_stock(player: Player, items_list: List[Type[Item]]) -> float:
    """Calculate stock held prior to clicking advance"""
    if player.round_number == 1:
        # * Use initial quantity purchased for final_stock
        return sum([item.quantity for item in items_list])
    # * Fetch previous period's final stock and add new quantity purchased
    return player.in_round(player.round_number - 1).final_stock + sum(
        [item.quantity for item in items_list]
    )


def calculate_interest_earned(player: Player) -> float:
    """Calculate interest earned on savings from prior period"""
    if player.round_number == 1:
        # * Calculate interest rate (without monetary policy)
        return 0
    return player.in_round(player.round_number - 1).final_savings * (
        C.INTEREST_RATE
        + (
            C.MONETARY_POLICY
            * C.INFLATION_DICT[player.round_number - 1][
                str(player.participant.inflation[(player.participant.round - 1)])
            ]
        )
    )


def calculate_real_interest(player: Player) -> float:
    """Calculate real interest rate (rather than nominal)"""
    if player.round_number == 1:
        return round(
            100
            * (
                C.INTEREST_RATE
                - C.INFLATION_DICT[player.round_number][
                    str(player.participant.inflation[(player.participant.round - 1)])
                ]
            ),
            2,
        )
    return round(
        100
        * (
            (
                C.INTEREST_RATE
                + (
                    C.MONETARY_POLICY
                    * C.INFLATION_DICT[player.round_number - 1][
                        str(
                            player.participant.inflation[(player.participant.round - 1)]
                        )
                    ]
                )
            )
            - C.INFLATION_DICT[player.round_number][
                str(player.participant.inflation[(player.participant.round - 1)])
            ]
        ),
        2,
    )


def create_decision_dict(
    items_list: List[Type[Item]],
) -> Dict[str, List[Union[List[str], List[int], List[float]]]]:
    """Generate dictionary with of purchase decision with item, quantity, and price"""
    return json.dumps(
        {
            "item": [item.sku for item in items_list],
            "quantity": [item.quantity for item in items_list],
            "price": [float(item.unit_price) for item in items_list],
        }
    )


def total_price(item: Type[Item]) -> float:
    """Calculate total price of item with quantity selected"""
    return item.quantity * item.unit_price


def to_dict(item: Type[Item]) -> Dict[str, Union[str, int, float]]:
    """Convert information about items into a dictionary"""
    return dict(
        sku=item.sku,
        name=item.name,
        quantity=item.quantity,
        total_price=total_price(item),
    )


def live_method(player: Player, data: Dict[str, int]) -> None:
    """Send info to HTML components related to savings and consumption decisions"""
    # * Calculate new price
    player.new_price = calculate_price(player)

    # * Add and remove from shopping cart
    change_quantity_in_cart(player, data)
    items = Item.filter(player=player)
    item_dicts = [to_dict(item) for item in items]

    player.total_price = sum([total_price(item) for item in items])
    player.initial_savings = calculate_initial_savings(player)
    player.final_stock = calculate_final_stock(player, items)
    player.interest_earned = calculate_interest_earned(player)
    player.real_interest = calculate_real_interest(player)
    player.cash_on_hand = player.initial_savings + C.INCOME
    player.final_savings = player.cash_on_hand - player.total_price
    player.decision = create_decision_dict(items)

    return {
        player.id_in_group: dict(
            items=item_dicts,
            total_price=player.total_price,
            initial_savings=player.initial_savings,
            interest_earned=player.interest_earned,
            cash_on_hand=player.cash_on_hand,
            final_savings=player.final_savings,
            final_stock=player.final_stock,
            decision=player.decision,
            new_price=player.new_price,
            real_interest=player.real_interest,
        )
    }


def average_early_stock(player: Type[Player]) -> float:
    """Calculate average stock before first high inflation phase"""
    participant = player.participant
    current_round = participant.round
    inflation = participant.inflation[current_round - 1]
    before = 12 if inflation == 1012 else 30
    stock_values = [v.final_stock for v in player.in_rounds(1, before)]
    if -1 in stock_values:
        b_index = stock_values.index(-1)
        stock_values = stock_values[:b_index]
    average_stock = statistics.mean(stock_values)
    return average_stock


def calculate_late_stock(player: Type[Player]) -> int:
    """Determine how many units were purchase late"""
    participant = player.participant
    current_round = participant.round
    inflation = participant.inflation[current_round - 1]
    before = 12 if inflation == 1012 else 30
    after = before + C.LATE_WINDOW
    end = C.NUM_ROUNDS
    if player.round_number >= before:
        stock_up = end - before - player.in_round(before).final_stock
    else:
        stock_up = 0
    # Adjust late stock with pre-defined window of time for subjects
    # to recognize inflation change
    if stock_up > 0 and player.in_round(after).final_stock == -1:
        late = stock_up - player.in_round(after).final_stock
    if stock_up > 0:
        late = stock_up - player.in_round(after).final_stock
    else:
        late = 0
    return late


def determine_errors(player: Type[Player]) -> Dict[str, float]:
    """Identify which errors the subject committed"""
    end = C.NUM_ROUNDS
    errors = ["early", "late", "excess"]
    early = average_early_stock(player)
    late = calculate_late_stock(player)
    excess = player.in_round(end).final_stock
    return dict(zip(errors, [early, late, excess]))


def determine_task_round_text(player: Type[Player]) -> str:
    """Determine which round the subject is currently on"""
    task_round = player.participant.round
    if task_round == SESSION_CONFIG_DEFAULTS["exp_length_rounds"]:
        return Lexicon.last_round
    elif task_round == 1:
        return Lexicon.first_round
    elif task_round == 2:
        suffix = Lexicon.second
        return Lexicon.round.format(task_round, suffix)
    elif task_round == 3:
        suffix = Lexicon.third
        return Lexicon.round.format(task_round, suffix)
    else:
        suffix = Lexicon.nth
        return Lexicon.round.format(task_round, suffix)


# PAGES
class MyPage(Page):
    """Main screen for player to buy goods and see their savings balance,
    inflation rate, salary, stock of goods and interests recieved"""

    live_method = live_method
    form_model = "player"
    form_fields = ["response_time"]

    @staticmethod
    def error_message(player, value):
        "Message saying insufficient cash"
        if player.final_savings < 0:
            return Lexicon.error_task_insufficient_cash.format(Lexicon.total_cash)

    @staticmethod
    def before_next_page(player: Type[Player], timeout_happened: bool) -> None:
        """Moves to next round after timeout happened"""
        participant = player.participant
        participant.periods_survived = player.round_number
        player.final_stock -= 1

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Send values from this __init__ script to Django components in the HTML"""
        interest_rate = {"real": False, "nominal": True}
        task_int = {"int": False}
        if player.round_number > 1 and player.final_stock == 0:
            player.final_stock = player.in_round(player.round_number - 1).final_stock
        return dict(
            income=cu(C.INCOME),
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            Lexicon=Lexicon,
            **which_language,
        )


class Survey1(Page):
    """Asks player their qualitative perception of how much prices changed"""

    form_model = "player"
    form_fields = ["qualitative_estimate"]
    timeout_seconds = C.TIME_LIMIT

    @staticmethod
    def is_displayed(player: Type[Player]) -> bool:
        """Page only displays every 12 months"""
        return player.round_number % 12 == 0

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Send values from this __init__ script to Django components in the HTML"""
        return dict(
            rounds12Before=player.round_number - 11, Lexicon=Lexicon, **which_language
        )


class Survey2(Page):
    """Asks subject their quantitative perception of inflation in %"""

    form_model = "player"
    form_fields = ["inf_estimate"]
    timeout_seconds = C.TIME_LIMIT

    @staticmethod
    def is_displayed(player) -> None:
        """Page only displays every 12 months if the participants responds to
        qualitative estimate that they believe prices changed"""
        return player.round_number % 12 == 0 and player.qualitative_estimate != 0

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Send values from this __init__ script to Django components in the HTML"""
        return dict(
            rounds12Before=player.round_number - 11, Lexicon=Lexicon, **which_language
        )


class Survey3(Page):
    "Qualitative inflation expectation question"
    form_model = "player"
    form_fields = ["qualitative_expectation"]
    timeout_seconds = C.TIME_LIMIT

    @staticmethod
    def is_displayed(player: Type[Player]) -> bool:
        """Page only displays every 12 months as well as after month 1"""
        return (
            player.round_number == 1
            or player.round_number % 12 == 0
            and player.round_number != C.NUM_ROUNDS
        )

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Send values from this __init__ script to Django components in the HTML"""
        return dict(
            rounds12Before=player.round_number - 11, Lexicon=Lexicon, **which_language
        )


class Survey4(Page):
    "Asks subject their quantitative expectation of inflation in %"
    form_model = "player"
    form_fields = ["inf_expectation"]
    timeout_seconds = C.TIME_LIMIT

    @staticmethod
    def is_displayed(player: Type[Player]) -> bool:
        """Page only displays every 12 months as well as after month 1 if the
        participants responds to qualitative estimate that they believe prices
        changed"""
        return (player.round_number == 1 and player.qualitative_expectation != 0) or (
            player.round_number % 12 == 0
            and player.round_number != C.NUM_ROUNDS
            and player.qualitative_expectation != 0
        )

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Send values from this __init__ script to Django components in the HTML"""
        return dict(
            rounds12Before=player.round_number - 11, Lexicon=Lexicon, **which_language
        )


class Failed(Page):
    "Page displayed when subject fails to survive until the end of the Saving Game"

    @staticmethod
    def is_displayed(player: Type[Player]) -> bool:
        "Displayed if subject advances with a stock or savings balance less than 0"
        return (
            player.in_round(player.round_number).final_stock < 0
            or player.in_round(player.round_number).final_savings < 0
        )

    @staticmethod
    def app_after_this_page(
        player: Type[Player], upcoming_apps: List[str]
    ) -> Union[str, None]:
        "Directs subject to the results app, `intervention_2`"
        return "intervention_2"

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Send values from this __init__ script to Django components in the HTML"""
        return dict(Lexicon=Lexicon, **which_language)

    @staticmethod
    def before_next_page(player: Type[Player], timeout_happened: bool) -> None:
        "Store data to PARTICIPANT_FIELDS to access in other apps, like `session_resulst`"
        participant = player.participant
        participant.periods_survived = player.round_number
        print(
            "participant.periods_survived=player.round_number: ",
            participant.periods_survived,
        )
        # Record payoff
        participant.task_results = 0
        print("results recorded: ", participant.task_results)
        setattr(participant, f"task_results_{participant.round}", float(0))
        print(
            "final recorded result (failed): ",
            getattr(participant, f"task_results_{participant.round}"),
        )
        ## Save number of erroneous units in stock at each benchmark month
        error_dict = determine_errors(player)
        current_round = participant.round
        setattr(participant, f"errors_{current_round}", error_dict)
        print(getattr(participant, f"errors_{current_round}"))
        print("this is the error", error_dict)


class Results(Page):
    """Dsplay game results"""

    @staticmethod
    def is_displayed(player: Type[Player]) -> bool:
        """Dislays page if game finished"""
        return player.round_number == C.NUM_ROUNDS

    # display final results
    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        """Send values from this __init__ script to Django components in the HTML"""
        round_text = determine_task_round_text(player)
        print(f"task_round: {round_text}")

        return dict(
            round_text=round_text,
            final_results=player.final_savings,
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def before_next_page(player: Type[Player], timeout_happened: bool) -> None:
        """Store data to PARTICIPANT_FIELDS to access in other apps, like `session_resulst`"""
        participant = player.participant

        participant.task_results = float(player.final_savings)
        setattr(
            participant,
            f"task_results_{participant.round}",
            float(player.final_savings),
        )
        print(
            "Current recorded result: ",
            getattr(participant, f"task_results_{participant.round}"),
        )
        ## Save number of erroneous units in stock at each benchmark month
        error_dict = determine_errors(player)
        current_round = participant.round
        setattr(participant, f"errors_{current_round}", error_dict)
        print(getattr(participant, f"errors_{current_round}"))


page_sequence = [
    MyPage,
    Failed,
    Survey1,
    Survey2,
    Survey3,
    Survey4,
    Results,
]
