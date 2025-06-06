from otree.api import *
from decimal import *
from settings import (
    SESSION_CONFIG_DEFAULTS,
    SESSION_CONFIGS,
    PARTICIPANT_FIELDS,
    LANGUAGE_CODE,
)

author = "Nathaniel Archer Lawrence, LEMMA, Université Panthéon-Assas - Paris II"
doc = """
Consumption simulation with interface based off of 'Shopping app (online grocery store)' from oTree demos,
see: <https://s3.amazonaws.com/otreehub/browsable_source/d7188187-cdba-4c61-ae3a-d7cc3d6fcde9/shop/index.html>.
"""

if LANGUAGE_CODE == "fr":
    from _static.lexicon_fr import Lexicon
else:
    from _static.lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {"en": False, "fr": False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


def read_csv():
    import csv

    f = open(__name__ + "/catalog.csv", encoding="utf-8-sig")
    rows = [row for row in csv.DictReader(f)]
    for row in rows:
        # all values in CSV are string unless you convert them
        row["unit_price"] = float(row["unit_price"])
        # translate name of good
        row["name"] = Lexicon.food
    return rows


class C(BaseConstants):
    NAME_IN_URL = "cx"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_QUESTIONS = 9 + 2

    # task constants
    NUM_PERIODS = SESSION_CONFIG_DEFAULTS["task_duration"]
    INITIAL_ENDOWMENT = SESSION_CONFIG_DEFAULTS["initial_endowment"]
    INCOME = SESSION_CONFIG_DEFAULTS["income"]
    INTEREST_RATE = SESSION_CONFIG_DEFAULTS["interest_rate"]
    INTEREST_PERCENT = round(INTEREST_RATE * 100, 2)
    INTEREST_ROUNDED = round(INTEREST_RATE, 4)
    INTEREST_EARNED = cu((INITIAL_ENDOWMENT + INCOME) * INTEREST_RATE)
    CONSUMPTION_RATE = 1  # amount of good consumed from stock balance each period
    MONETARY_POLICY = SESSION_CONFIG_DEFAULTS["monetary_policy"]
    TOTAL_CASH = cu(INITIAL_ENDOWMENT + INCOME)

    # list of products taken from csv file
    PRODUCTS = read_csv()
    # SKU = 'stock keeping unit' = product ID
    PRODUCTS_DICT = {row["sku"]: row for row in PRODUCTS}

    # For practice questions
    QUANTITY = 4
    QUANTITY_SAVINGS = QUANTITY - 2
    NEW_CASH = TOTAL_CASH - (PRODUCTS_DICT["1"]["unit_price"] * QUANTITY_SAVINGS)
    NEW_STOCK = 0
    NEW_STOCK_3 = 0
    NEW_STOCK_4 = 2
    NEW_STOCK_5 = 0
    NEW_STOCK_6 = 0
    NEW_STOCK_7 = 0
    NEW_STOCK_8 = 0

    # Define if Real or Nominal Interest Rate is displayed
    REAL = False
    NOMINAL = True
    INT = True


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ## choices = [[value, label],[value, label],...]

    intro_1 = models.IntegerField(
        label=Lexicon.task_int_intro_1, widget=widgets.RadioSelect
    )
    # Counts number of attempts for question
    intro_1_errors = models.IntegerField(initial=0)
    q1 = models.IntegerField(label="", widget=widgets.RadioSelect)
    q1_errors = models.IntegerField(initial=0)
    q2 = models.IntegerField(label="", widget=widgets.RadioSelect)
    q2_errors = models.IntegerField(initial=0)
    q3 = models.IntegerField(label="", widget=widgets.RadioSelect)
    q3_errors = models.IntegerField(initial=0)
    q4 = models.IntegerField(label="", widget=widgets.RadioSelect)
    q4_errors = models.IntegerField(initial=0)
    q5 = models.IntegerField(label="", widget=widgets.RadioSelect)
    q5_errors = models.IntegerField(initial=0)
    q6 = models.IntegerField(label="", widget=widgets.RadioSelect)
    q6_errors = models.IntegerField(initial=0)
    q7 = models.IntegerField(label="", widget=widgets.RadioSelect)
    q7_errors = models.IntegerField(initial=0)
    q8 = models.IntegerField(
        label="",
        choices=[
            [0, Lexicon.save],
            [1, Lexicon.buy_1],
            [2, Lexicon.buy_x.format(2, Lexicon.units)],
            [3, Lexicon.buy_x.format(3, Lexicon.units)],
            [4, Lexicon.buy_x.format(4, Lexicon.units)],
            [5, Lexicon.buy_x.format(5, Lexicon.units)],
            [6, Lexicon.buy_more_than.format(5, Lexicon.units)],
        ],
        widget=widgets.RadioSelect,
    )
    q8_errors = models.IntegerField(initial=0)

    total_price = models.CurrencyField(initial=0)
    initial_savings = models.CurrencyField(initial=0)
    cashOnHand = models.CurrencyField(initial=0)
    finalSavings = models.CurrencyField(initial=0)
    finalStock = models.IntegerField(initial=0)
    interestEarned = models.CurrencyField(initial=0)
    newPrice = models.FloatField(initial=C.PRODUCTS_DICT["1"]["unit_price"])


def intro_1_choices(player):
    import random

    choices = [
        [1, Lexicon.task_int_intro_1_rising_price],
        [2, Lexicon.interest_rate],
        [3, Lexicon.task_int_intro_1_rising_salary],
        [4, Lexicon.none_of_the_above],
    ]
    random.shuffle(choices)
    return choices


def q1_choices(player):
    import random

    choices = [[1, Lexicon.more], [2, Lexicon.less], [3, Lexicon.the_same_amount]]
    random.shuffle(choices)
    return choices


def q2_choices(player):
    import random

    choices = [
        [1, Lexicon.stock_up],
        [2, Lexicon.save],
        [3, Lexicon.buy_1],
    ]
    random.shuffle(choices)
    return choices


def q3_choices(player):
    import random

    choices = [[1, Lexicon.more], [2, Lexicon.less], [3, Lexicon.the_same_amount]]
    random.shuffle(choices)
    return choices


def q4_choices(player):
    import random

    choices = [
        [1, Lexicon.stock_up],
        [2, Lexicon.save],
        [3, Lexicon.buy_1],
    ]
    random.shuffle(choices)
    return choices


def q5_choices(player):
    import random

    choices = [[1, Lexicon.more], [2, Lexicon.less], [3, Lexicon.the_same_amount]]
    random.shuffle(choices)
    return choices


def q6_choices(player):
    import random

    choices = [
        [1, Lexicon.stock_up],
        [2, Lexicon.save],
        [3, Lexicon.buy_1],
    ]
    random.shuffle(choices)
    return choices


def q7_choices(player):
    import random

    choices = [[1, Lexicon.more], [2, Lexicon.less], [3, Lexicon.the_same_amount]]
    random.shuffle(choices)
    return choices


class Item(ExtraModel):
    player = models.Link(Player)
    sku = models.StringField()
    name = models.StringField()
    quantity = models.IntegerField()
    unit_price = models.CurrencyField()
    newPrice = models.FloatField(initial=C.PRODUCTS_DICT["1"]["unit_price"])


# Calculate total price of item with quantity selected


def total_price(item: Item):
    return item.quantity * item.unit_price


# Convert information about items into a dictionary


def to_dict(item: Item):
    return dict(
        sku=item.sku,
        name=item.name,
        quantity=item.quantity,
        total_price=total_price(item),
    )


# Send info to HTML


def live_method(player: Player, data):

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
class Int_intro_1(Page):
    counter_questions = 0

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class Int_intro_2(Page):
    form_model = "player"
    form_fields = ["intro_1"]
    counter_questions = Int_intro_1.counter_questions + 1

    @staticmethod
    def vars_for_template(player: Player):
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=cu(C.INCOME),
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(
                Int_intro_2.counter_questions / C.NUM_QUESTIONS * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            intro_1=1,
        )

        error_messages = dict(intro_1=Lexicon.error_task_int_intro_1)

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages = error_messages[field_name]
                setattr(
                    player,
                    f"{field_name}_errors",
                    getattr(player, f"{field_name}_errors") + 1,
                )
                print(f"{field_name}_errors: ", getattr(player, f"{field_name}_errors"))
                return error_messages


class Int_intro_3(Page):
    # form_model = 'player'
    # form_fields = ['intro_2']
    counter_questions = Int_intro_2.counter_questions + 1

    @staticmethod
    def vars_for_template(player: Player):
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=cu(C.INCOME),
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            # For progress bars
            percentage=round(
                Int_intro_3.counter_questions / C.NUM_QUESTIONS * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


class Int_3(Page):
    live_method = live_method
    form_model = "player"
    form_fields = ["q1", "q2"]

    counter_questions = Int_intro_3.counter_questions + 1

    @staticmethod
    def vars_for_template(player: Player):
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=cu(C.INCOME),
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            stock=C.NEW_STOCK_3,
            # For progress bars
            percentage=round(
                Int_3.counter_questions / C.NUM_QUESTIONS * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(q1=2, q2=1)

        error_messages = dict(
            q1=Lexicon.error_task_int_q1,
            q2=Lexicon.error_task_int_q2,
        )

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages = error_messages[field_name]
                setattr(
                    player,
                    f"{field_name}_errors",
                    getattr(player, f"{field_name}_errors") + 1,
                )
                print(f"{field_name}_errors: ", getattr(player, f"{field_name}_errors"))
                return error_messages


class Int_4(Page):
    live_method = live_method
    form_model = "player"
    form_fields = ["q3", "q4"]

    counter_questions = Int_3.counter_questions + len(Int_3.form_fields)

    @staticmethod
    def vars_for_template(player: Player):
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=cu(C.INCOME),
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            stock=C.NEW_STOCK_4,
            # For progress bars
            percentage=round(
                Int_4.counter_questions / C.NUM_QUESTIONS * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(q3=1, q4=2)

        error_messages = dict(
            q3=Lexicon.error_task_int_q3, q4=Lexicon.error_task_int_q4
        )

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages = error_messages[field_name]
                setattr(
                    player,
                    f"{field_name}_errors",
                    getattr(player, f"{field_name}_errors") + 1,
                )
                print(f"{field_name}_errors: ", getattr(player, f"{field_name}_errors"))
                return error_messages


class Int_5(Page):
    live_method = live_method
    form_model = "player"
    form_fields = ["q5", "q6"]

    counter_questions = Int_4.counter_questions + len(Int_4.form_fields)

    @staticmethod
    def vars_for_template(player: Player):
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=cu(C.INCOME),
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            stock=C.NEW_STOCK_5,
            # For progress bars
            percentage=round(
                Int_5.counter_questions / C.NUM_QUESTIONS * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(q5=1, q6=3)

        error_messages = dict(
            q5=Lexicon.error_task_int_q5, q6=Lexicon.error_task_int_q6
        )

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages = error_messages[field_name]
                setattr(
                    player,
                    f"{field_name}_errors",
                    getattr(player, f"{field_name}_errors") + 1,
                )
                print(f"{field_name}_errors: ", getattr(player, f"{field_name}_errors"))
                return error_messages


class Int_6(Page):
    live_method = live_method
    form_model = "player"
    form_fields = ["q7", "q8"]

    counter_questions = Int_5.counter_questions + len(Int_5.form_fields)

    @staticmethod
    def vars_for_template(player: Player):
        interest_rate = {"real": C.REAL, "nominal": C.NOMINAL}
        task_int = {"int": C.INT}
        return dict(
            income=cu(C.INCOME),
            **interest_rate,
            nominal_interest_rate=round((C.INTEREST_RATE * 100), 2),
            **task_int,
            stock=C.NEW_STOCK_6,
            # For progress bars
            percentage=round(
                Int_6.counter_questions / C.NUM_QUESTIONS * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(q7=2, q8=4)

        error_messages = dict(
            q7=Lexicon.error_task_int_q7, q8=Lexicon.error_task_int_q8
        )

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages = error_messages[field_name]
                setattr(
                    player,
                    f"{field_name}_errors",
                    getattr(player, f"{field_name}_errors") + 1,
                )
                print(f"{field_name}_errors: ", getattr(player, f"{field_name}_errors"))
                return error_messages


class Results(Page):

    counter_questions = Int_6.counter_questions + len(Int_6.form_fields)

    # For progress bars
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            percentage=round(
                Results.counter_questions / C.NUM_QUESTIONS * 100,
            ),
            Lexicon=Lexicon,
            **which_language,
        )


page_sequence = [
    Int_intro_1,
    Int_intro_2,
    Int_intro_3,
    Int_3,
    Int_4,
    Int_5,
    Int_6,
    Results,
]
