import csv
from typing import List, Dict, Union, Type
import random
from itertools import count
from decimal import *

from otree.api import *

from settings import SESSION_CONFIG_DEFAULTS, LANGUAGE_CODE

author = "Nathaniel Archer Lawrence"
doc = """Interactive instructions for The Savings Game"""

if LANGUAGE_CODE == "fr":
    from _static.lexicon_fr import Lexicon
else:
    from _static.lexicon_en import Lexicon


# * This is the dict you should pass to each page in vars_for_template,
# * enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {"en": False, "fr": False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True

# * Dict to pass whether participant receives instructions treatment or not
# * (treatment = no info on food price changes)
instructions = {"treat": False, "control": False}


def read_csv_catalog() -> List[Dict[str, Union[str, float]]]:
    """Convert csv with product catalog to dict"""
    with open(__name__ + "/catalog.csv", encoding="utf-8-sig") as file:
        f = file
        rows = [row for row in csv.DictReader(f)]
        for row in rows:
            # all values in CSV are string unless you convert them
            row["unit_price"] = float(row["unit_price"])
            # translate name of good
            row["name"] = Lexicon.food
        return rows


class C(BaseConstants):
    "defines the url name of the page"

    NAME_IN_URL = "instructions"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_PAGES = 9

    # Remuneration constants
    PARTICIPATION_FEE = int(
        SESSION_CONFIG_DEFAULTS["participation_fee"]
        / SESSION_CONFIG_DEFAULTS["conversion_factor"]
    )
    CONVERSION_FACTOR = SESSION_CONFIG_DEFAULTS["conversion_factor"]
    EUROS_EXAMPLE = 10
    CONVERTED_EXAMPLE = CONVERSION_FACTOR * EUROS_EXAMPLE
    # CORRECT_ANSWER_FEE = cu(
    #     SESSION_CONFIG_DEFAULTS["correct_answer_fee"] * CONVERSION_FACTOR
    # )
    TIME_LIMIT = SESSION_CONFIG_DEFAULTS["time_limit"]

    # task constants
    NUM_PERIODS = SESSION_CONFIG_DEFAULTS["task_duration"]
    INITIAL_ENDOWMENT = cu(SESSION_CONFIG_DEFAULTS["initial_endowment"])
    INCOME = SESSION_CONFIG_DEFAULTS["income"]
    INTEREST_RATE = SESSION_CONFIG_DEFAULTS["interest_rate"]
    INTEREST_PERCENT = round(INTEREST_RATE * 100, 2)
    INTEREST_ROUNDED = round(INTEREST_RATE, 4)
    INTEREST_EARNED = cu((INITIAL_ENDOWMENT + INCOME) * INTEREST_RATE)
    CONSUMPTION_RATE = 1  # amount of good consumed from stock balance each period
    MONETARY_POLICY = SESSION_CONFIG_DEFAULTS["monetary_policy"]
    TOTAL_CASH = cu(INITIAL_ENDOWMENT + INCOME)

    # list of products taken from csv file
    PRODUCTS = read_csv_catalog()
    # SKU = 'stock keeping unit' = product ID
    PRODUCTS_DICT = {row["sku"]: row for row in PRODUCTS}

    # For practice questions
    QUANTITY = 4
    QUANTITY_SAVINGS = QUANTITY - 2
    NEW_CASH = TOTAL_CASH - (PRODUCTS_DICT["1"]["unit_price"] * QUANTITY_SAVINGS)
    NEW_STOCK = 1
    ESTIMATE_PRACTICE = 1

    # Define if Real or Nominal Interest Rate is displayed
    REAL = False
    NOMINAL = True
    INT = False


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    "Register players answers to questions"

    # Capture time it takes to complete the Instructions
    startTime = models.FloatField(initial=0)
    endTime = models.FloatField(initial=0)

    # choices = [[value,label],[value,label],...]
    q1 = models.IntegerField(label=Lexicon.q1, widget=widgets.RadioSelect)
    # Counts number of attempts for question
    q1_errors = models.IntegerField(initial=0)

    q2 = models.IntegerField(label=Lexicon.q2, widget=widgets.RadioSelect)
    q2_errors = models.IntegerField(initial=0)

    q3 = models.IntegerField(label=Lexicon.q3, widget=widgets.RadioSelect)
    q3_errors = models.IntegerField(initial=0)

    q4 = models.IntegerField(label=Lexicon.q4, widget=widgets.RadioSelect)
    q4_errors = models.IntegerField(initial=0)

    # Check: Select given quantity
    q8 = models.FloatField()
    q8_errors = models.IntegerField(initial=0)

    # Check: Select for given Final Savings
    q9 = models.FloatField()
    q9_errors = models.IntegerField(initial=0)

    # Check: Select for given Stock
    q10 = models.IntegerField()
    q10_errors = models.IntegerField(initial=0)

    q11 = models.IntegerField(label=Lexicon.q11, widget=widgets.RadioSelect)
    q11_errors = models.IntegerField(initial=0)

    # Required to make the interactive game screen work
    total_price = models.CurrencyField(initial=0)
    initial_savings = models.CurrencyField(initial=0)
    cashOnHand = models.CurrencyField(initial=0)
    finalSavings = models.CurrencyField(initial=0)
    finalStock = models.IntegerField(initial=0)
    interestEarned = models.CurrencyField(initial=0)
    newPrice = models.FloatField(initial=C.PRODUCTS_DICT["1"]["unit_price"])


def q1_choices(player: Type[Player]) -> List[List[Union[int, str]]]:
    """Randomize order of choices"""
    print("player is", type(player))
    choices = [
        [1, Lexicon.savings_account],
        [2, Lexicon.stock],
        [3, Lexicon.total_cash],
        [4, Lexicon.q1_choice_4],
    ]
    random.shuffle(choices)
    return choices


def q2_choices(player: Type[Player]) -> List[List[Union[int, str]]]:
    """Randomize order of choices"""
    choices = [[1, "1"], [2, "0"], [3, "3"], [4, "120"]]
    random.shuffle(choices)
    return choices


def q3_choices(player: Type[Player]) -> List[List[Union[int, str]]]:
    """Randomize order of choices"""
    choices = [
        [1, Lexicon.no],
        [2, Lexicon.yes],
        [3, Lexicon.q3_choice_3],
        [4, Lexicon.q3_choice_4],
    ]
    random.shuffle(choices)
    return choices


def q4_choices(player: Type[Player]) -> List[List[Union[int, str]]]:
    """Randomize order of choices"""
    choices = [
        [1, cu(130)],
        [2, cu(110)],
        [3, cu(120)],
        [4, cu(100)],
        [5, Lexicon.q4_choice_5],
    ]
    random.shuffle(choices)
    return choices


def q11_choices(player: Type[Player]) -> List[List[Union[int, str]]]:
    """Randomize order of choices"""
    choices = [
        [1, Lexicon.q11_choice_1],
        [2, Lexicon.q11_choice_2],
        [3, Lexicon.q11_choice_3],
        [4, Lexicon.q11_choice_4],
    ]
    random.shuffle(choices)
    return choices


# def calc_C.NUM_PAGES(player):
#     """Calculate number of questions for progress bar per treatment group"""
#     if player.participant.instructions == "treat":
#         C.NUM_PAGES = C.C.NUM_PAGES
#     else:
#         C.NUM_PAGES = C.C.NUM_PAGES + 1
#     return C.NUM_PAGES


class Item(ExtraModel):
    """Custom class for the product information"""

    player = models.Link(Player)
    sku = models.StringField()
    name = models.StringField()
    quantity = models.IntegerField()
    unit_price = models.CurrencyField()
    newPrice = models.FloatField(initial=C.PRODUCTS_DICT["1"]["unit_price"])


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


def live_method(player: Type[Player], data) -> Dict[
    str,
    Dict[
        str,
        Union[Dict[str, Union[str, int, Type[Currency]]], float, int, Type[Currency]],
    ],
]:
    """Send info to HTML components"""
    if player.round_number == 1:
        player.newPrice = float(C.PRODUCTS_DICT["1"]["unit_price"])
        if "sku" in data:
            sku = data["sku"]
            delta = data["delta"]
            product = C.PRODUCTS_DICT[sku]
            matches = Item.filter(player=player, sku=sku)
            if matches:
                [item] = matches
                item.quantity += delta
                if item.quantity <= 0:
                    item.delete()
            else:
                if delta > 0:
                    Item.create(
                        player=player,
                        quantity=delta,
                        sku=sku,
                        name=product["name"],
                        unit_price=player.newPrice,
                    )

        items = Item.filter(player=player)
        item_dicts = [to_dict(item) for item in items]
        player.total_price = sum([total_price(item) for item in items])
        player.initial_savings = C.INITIAL_ENDOWMENT
        player.cashOnHand = player.initial_savings + C.INCOME
        player.finalSavings = player.cashOnHand - player.total_price
        player.finalStock = sum([item.quantity for item in items])
        player.interestEarned = 0
        player.newPrice = player.newPrice

    return {
        player.id_in_group: dict(
            items=item_dicts,
            total_price=player.total_price,
            initial_savings=player.initial_savings,
            interestEarned=player.interestEarned,
            cashOnHand=player.cashOnHand,
            finalSavings=player.finalSavings,
            finalStock=player.finalStock,
            newPrice=player.newPrice,
        )
    }


# PAGES
class Instructions_1(Page):
    "Defines the page instructions 1"

    form_model = "player"
    form_fields = ["startTime"]

    @staticmethod
    def vars_for_template(player: Type[Player]) -> Dict[str, Union[str, bool]]:
        return dict(Lexicon=Lexicon, **which_language)


class Instructions_2(Page):
    "Defines the page instructions 2"

    live_method = live_method

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(1 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )


class Instructions_3(Page):
    "Defines the page instructions 3"

    live_method = live_method
    form_model = "player"
    form_fields = ["q8"]

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            description_interest_rate=Lexicon.description_interest_rate,
            description_salary=Lexicon.description_salary,
            # For progress bars
            percentage=round(2 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player: Type[Player], values) -> Dict[str, str]:
        "defines an error in quantity registration for q8"
        solutions = dict(q8=C.QUANTITY)

        error_messages = dict(
            q8=Lexicon.error_task_instructions_q8.format(
                Lexicon.quantity,
                Lexicon.my_cart,
                C.QUANTITY,
                Lexicon.food,
                Lexicon.quantity,
                Lexicon.my_cart,
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


class Instructions_4(Page):
    "Defines the page instructions 4"

    live_method = live_method
    form_model = "player"
    form_fields = ["q9"]

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(3 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player: Type[Player], values) -> Dict[str, str]:
        "error messsage if submitted answer is in the wrong format for q9"
        solutions = dict(q9=float(C.NEW_CASH))

        error_messages = dict(
            q9=Lexicon.error_task_instructions_q9.format(
                Lexicon.savings_account,
                C.NEW_CASH,
                Lexicon.quantity,
                Lexicon.my_cart,
                Lexicon.savings_account,
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
                return error_messages


class Instructions_5(Page):
    "Defines the page instructions 5"

    live_method = live_method
    form_model = "player"
    form_fields = ["q10"]

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(4 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player: Type[Player], values) -> str:
        "error messsage if submitted answer is in the wrong format for q10"
        solutions = dict(q10=C.NEW_STOCK)

        error_messages = dict(
            q10=Lexicon.error_task_instructions_q10.format(
                Lexicon.stock,
                C.NEW_STOCK,
                Lexicon.quantity,
                Lexicon.my_cart,
                Lexicon.stock,
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


class Instructions_6(Page):
    "Defines the page instructions 6"

    form_model = "player"
    form_fields = ["q1"]

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(5 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player: Type[Player], values) -> str:
        "error messsage if submitted value doesn't match expected value for q1"
        solutions = dict(
            q1=1,
        )

        error_messages = dict(q1=Lexicon.error_task_instructions_general)

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


class Instructions_7(Page):
    "Defines the page instructions 7"

    form_model = "player"
    form_fields = ["q2"]

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            total_stock_needed=C.NUM_PERIODS + 1,
            # For progress bars
            percentage=round(6 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player: Type[Player], values) -> str:
        solutions = dict(
            q2=1,
        )

        error_messages = dict(q2=Lexicon.error_task_instructions_general)

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


class Instructions_8(Page):
    "Defines the page instructions 8"

    live_method = live_method
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Type[Player]):
        """Remove q11 about Food price change if in instructions treatment group"""
        if player.participant.instructions == "treat":
            form_fields = ["q3"]
        else:
            form_fields = ["q3", "q11"]
        return form_fields

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        ## Toggle price change instructions per treatment group
        if player.participant.instructions == "treat":
            instructions["treat"] = True
        else:
            instructions["control"] = True
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **instructions,
            # For progress bars
            percentage=round(7 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player: Type[Player], values) -> str:
        if player.participant.instructions == "treat":
            solutions = dict(q3=1)
        else:
            solutions = dict(q3=1, q11=2)

        error_messages = dict(
            q3=Lexicon.error_task_instructions_q3,
            q11=Lexicon.error_task_instructions_q11,
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


class Instructions_9(Page):
    "Defines the page instructions 9"

    live_method = live_method
    form_model = "player"
    form_fields = ["q4"]

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        ## Toggle total questions for progress bar per instructions treatment group
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        # ## Adjust for fact that number of form_fields not counted in Instructions_8
        # if player.participant.instructions == "treat":
        #     Instructions_9.counter_questions += 1
        # elif player.participant.instructions == "control":
        #     Instructions_9.counter_questions += 2
        # else:
        #     pass
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(8 / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player: Type[Player], values) -> str:
        solutions = dict(q4=1)

        error_messages = dict(q4=Lexicon.error_task_instructions_q4)

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


class Results(Page):
    "presents result of experiment"

    form_model = "player"
    form_fields = ["endTime"]

    @staticmethod
    def vars_for_template(
        player: Type[Player],
    ) -> Dict[str, Union[Type[Currency], float, str, bool]]:
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        # ## Adjust for fact that number of form_fields not counted in Instructions_8
        # if player.participant.instructions == "treat":
        #     Results.counter_questions += 1
        # elif player.participant.instructions == "control":
        #     Results.counter_questions += 2
        # else:
        #     pass
        return dict(
            income=C.INCOME,
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(C.NUM_PAGES / C.NUM_PAGES * 100),
            Lexicon=Lexicon,
            **which_language,
        )


page_sequence = [
    Instructions_1,
    Instructions_2,
    Instructions_3,
    Instructions_4,
    Instructions_5,
    Instructions_6,
    Instructions_7,
    Instructions_8,
    Instructions_9,
    Results,
]
