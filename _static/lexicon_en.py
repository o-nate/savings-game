from settings import SESSION_CONFIG_DEFAULTS


class Lexicon:
    """Define English terms here"""

    # task
    starting_balances = "Starting Balances"
    interest_earned_last_period = "Interest Earned Last Month"
    total_cash = "Total Cash"
    ending_balances = "Ending Balances"
    savings_account = "Savings Account"
    stock = "Stock"
    unit = "unit"
    units = "units"
    market_data = "Market Data"
    salary = "Salary"
    catalog = "Catalog"
    food = "Food"
    price = "Price"
    my_cart = "My Cart"
    name = "Name"
    quantity = "Quantity"
    prix_total = "Total price"
    finalize_purchase = "Finalize Purchase"
    total = "Total"
    slider_your_value = "Your estimate"
    cancel = "Cancel"

    warning_final_purch = f"""Warning! Your {stock} balance is currently 0. 
    If this is a mistake, please click Cancel and update {my_cart}. If you do 
    not have enough money, please click OK to end the game and proceed to the 
    additional tasks."""

    warning_final_purch_2 = f"""****Are you sure you do not want to survive?****
    • Click "{cancel}" to adjust {my_cart}.
    • Cliquez sur "OK" si vous voulez ne pas survivre."""

    qualitative_estimate = (
        """Do you find that, over the past twelve months, prices have..."""
    )

    qualitative_expectation_month_1 = """How do you 
    expect prices to evolve over the next twelve months?"""

    qualitative_expectation = """Given the past twelve months, how do you 
    expect prices to evolve over the next twelve months?"""

    qualitative_est_rapid = "Increased rapidly"
    qualitative_est_moderate = "Increased moderately"
    qualitative_est_slight = "Increased slightly"
    qualitative_est_same = "Stayed the same"
    qualitative_est_decrease = "Decreased"

    ## For month 1
    qualitative_exp_rapid_month_1 = "They will increase quickly"
    qualitative_exp_moderate_month_1 = "They will increase moderately"
    qualitative_exp_slight_month_1 = "They will increase slowly"
    qualitative_exp_same_month_1 = "They will stay the same"
    qualitative_exp_decrease_month_1 = "They will decrease"

    qualitative_exp_rapid = "They will increase more quickly"
    qualitative_exp_moderate = "They will continue at the same rate"
    qualitative_exp_slight = "They will increase less quickly"
    qualitative_exp_same = "They will stay the same"
    qualitative_exp_decrease = "They will decrease"

    inf_estimate = """By what percentage do you think prices increased 
    (or decreased) over the past twelve months? (Give a value in %)"""

    inf_expectation = """By what percentage do you think prices will increase 
    (or decrease) over the next twelve months? (Give a value in %)"""

    slider = "Slider"

    # General expressions
    game = "Savings Game"
    I_do_not_know = "I do not know"
    yes = "Yes"
    no = "No"
    maybe = "Maybe"
    somewhat = "Somewhat"
    true = "True"
    false = "False"
    not_applicable = "Not applicable"
    more = "More"
    less = "Less"
    the_same_amount = "The same amount"
    more_money = "More money"
    less_money = "Less money"
    same_money = "The same amount of money"
    none_of_the_above = "None of the above"
    next = "Next"
    click_next = """Click the Next button below to proceed."""
    round = "{} round"
    first_round = "first round"
    last_round = "last round"
    second = "nd"
    third = "rd"
    nth = "th"
    completed_questionnaire = "You have completed the questionnaire. Please, click the Next button below to proceed."
    completed_game_round = """You have now completed today's round of the game. Click the Next button below to proceed to the follow-up questions."""
    completed_task_round = """You have now completed today's round of the game and follow-up questions. Click the Next button below to proceed."""
    slider = "Slider"

    sliders_instructions = f"""Click the blue bar to reveal the 
    {slider}. Drag it along the bar to select your estimate with either 
    your mouse or the arrow keys on your keyboard."""

    remunerated_questions = "Remunerated Questions"
    increased = "Increased"
    decreased = "Decreased"
    stayed_same = "Stayed the same"
    increase = "Increase"
    decrease = "Decrease"
    stay_same = "Stay the same"
    no_change = "No change"
    it_increases = "It increases."
    it_decreases = "It decreases."
    it_stays_the_same = "It stays the same."
    not_enough_info = "There is not enough information to determine the effect."
    instructions = "Instructions"
    correct = "That is correct."
    interest_rate = "Interest Rate"
    nominal_interest_rate = "Nominal Interest Rate"
    real_interest_rate = "Real Interest Rate"
    completed_so_far = "Completed so far"
    inflation_rate = "Inflation Rate"
    purchasing_power = "Purchasing Power"
    comprehension = "Comprehension"
    stock_up = f"Buy more than 1 {unit}"
    save = "Save"
    buy_1 = f"Buy 1 {unit}"
    buy_x = "Buy {} {}"
    buy_more_than = "Buy more than {} {}"

    # init
    wait_for_next_button = """The "Next" button will appear momentarily"""
    redirected = "You will be redirected to the experiment page."

    # redirectapp
    important_reminder = "Important reminder:"
    please_wait = "Please wait..."
    session_tomorrow = "The next session will take place tomorrow."
    thank_you_for_participation = "Thank you for your participation in today's session."
    continue_button = "Continue"

    # task_instructions
    description_months = f"""Here you see how many months remain in the 
    game. It last {SESSION_CONFIG_DEFAULTS['task_duration']} Months in total."""

    description_interest_earned_last_period = "This shows how much interest you earned on your Savings Account in the previous month."
    description_total_cash = (
        "Total Cash is how much money you have to spend each month on Food."
    )
    description_savings_account = "This shows you how much money you will keep for the next month after clicking Finalize Purchase at the bottom. It is also how much you will earn interest on."
    description_stock = "Here, you see how much Food you will have this month."
    description_interest_rate = "The percentage of the total in your {} that will be added next month. This rate does not change during the game."
    description_salary = "An additional amount you receive each month. This amount does not change during the game."
    description_catalog = "Catalog displays the current price of Food. To add units of Food to My Cart, click the grey +1 button as many times as needed."
    description_my_cart = "My Cart shows you the Quantity of Food you have selected and the Total Price you will pay."
    q1 = "The final value of which of these balances determines your performance-based remuneration for the game?"

    q2 = f"""What is the minimum amount you must have in your {stock} 
    before clicking the "{finalize_purchase}" button to survive to the next 
    month?"""

    q3 = f"Can the {interest_rate} change during the game?"

    q4 = f"""Suppose a player had 100₮ in {savings_account} last month. 
    If they earn 10₮ in interest and receive 20₮ in monthly salary, what will 
    their {total_cash} be?"""

    q11 = f"""Can the price of {food} change?"""
    q1_choice_4 = "Interest earned"
    q3_choice_3 = f"It depends how much is in {savings_account}"
    q3_choice_4 = f"It depends how much is in {total_cash}"
    q4_choice_5 = "We do not have sufficient information to determine."
    q11_choice_1 = "It can increase and decrease."
    q11_choice_2 = "It can only increase"
    q11_choice_3 = "It can only decrease"
    q11_choice_4 = "It cannot change"

    # task_questions
    priceMemory = "What was the price in month"

    # task_int
    task_int_test_completed = "Congratulations, you have passed the comprehension test. We will now play the game again."
    task_int_f_q1 = "Suppose you face the current situation below. In this month, what happens to your purchasing power?"
    task_int_f_q2 = "Can you afford more, less, or the same amount of Food as before?"
    task_int_f_q3 = "Suppose you face the current situation below. In this month, what happens to your purchasing power?"
    task_int_f_q4 = "Can you afford more, less, or the same amount of Food as before?"
    task_int_f_q5 = "Suppose you face the current situation below. In this month, what happens to your purchasing power?"
    task_int_f_q6 = "Can you afford more, less, or the same amount of Food as before?"

    task_int_cx_intro_1 = f"""The {inflation_rate} is related to:"""
    task_int_cx_intro_1_rising_price = f"An increase in the price of {food}"
    task_int_cx_intro_1_rising_interest = f"An increase in the {interest_rate}"

    task_int_intro_1 = f"""The {inflation_rate} is related to:"""
    task_int_intro_1_rising_price = f"An increase in the price of {food}"
    task_int_intro_1_rising_interest = f"An increase in the {interest_rate}"

    task_int_q_qt = f""" Can you buy more, less, or the same amount of 
    {food} as before?"""

    task_int_q_do = "What should you do in the situation displayed below?"

    task_int_high_inf = "High inflation"
    task_int_low_inf = "Low inflation"

    task_int_explain = {
        "early": {
            3: {
                "true": """That is correct. It is important to resist the urge to stock up and sacrifice interest that can be earned. In the future, check whether you are in high or low inflation before stocking up.""",
                "false": """It appears that you did not have any cost due to stocking too early.""",
            },
            2: {
                "true": """That is correct. It appears that you did not have any cost due to stocking too early.""",
                "false": """It appears that you did have cost due to stocking too early. It is important to resist the urge to stock up and sacrifice interest that can be earned. In the future, check whether you are in high or low inflation before stocking up.""",
            },
            0: {
                "true": """It appears that you did have cost due to stocking too early. It is important to resist the urge to stock up and sacrifice interest that can be earned. In the future, check whether you are in high or low inflation before stocking up.""",
                "false": """It appears that you did not have any cost due to stocking too early. It is important to resist the urge to stock up and sacrifice interest that can be earned. In the future, check whether you are in high or low inflation before stocking up.""",
            },
        },
        "late": {
            3: {
                "true": """That is correct. It is important to act decisively when high inflation appears. Remember to pay attention to prices to check whether you are in high or low inflation.""",
                "false": """It appears that you did not have any cost due to not stocking enough.""",
            },
            2: {
                "true": """That is correct. It appears that you did not have any cost due to not stocking enough.""",
                "false": """It appears that you did have cost due to not stocking enough. It is important to act decisively when high inflation appears. Remember to pay attention to prices to check whether you are in high or low inflation.""",
            },
            0: {
                "true": """It appears that you did have cost due to not stocking enough. It is important to act decisively when high inflation appears. Remember to pay attention to prices to check whether you are in high or low inflation.""",
                "false": """It appears that you did not have any cost due to not stocking enough. It is important to act decisively when high inflation appears. Remember to pay attention to prices to check whether you are in high or low inflation.""",
            },
        },
        "excess": {
            3: {
                "true": f"""That is correct. It is important to pay attention to how much stock you need to survive through Month {SESSION_CONFIG_DEFAULTS["task_duration"]}. Your stock should never be greater than {SESSION_CONFIG_DEFAULTS["task_duration"] + 1}.""",
                "false": """It appears that you did not have any cost due to stocking too much.""",
            },
            2: {
                "true": """That is correct. It appears that you did not have any cost due to stocking too much.""",
                "false": f"""It appears that you did have cost due to stocking too much. It is important to pay attention to how much stock you need to survive through Month {SESSION_CONFIG_DEFAULTS["task_duration"]}. Your stock should never be greater than {SESSION_CONFIG_DEFAULTS["task_duration"] + 1}.""",
            },
            0: {
                "true": f"""It appears that you did have cost due to stocking too much. It is important to pay attention to how much stock you need to survive through Month {SESSION_CONFIG_DEFAULTS["task_duration"]}. Your stock should never be greater than {SESSION_CONFIG_DEFAULTS["task_duration"] + 1}.""",
                "false": """It appears that you did not have any cost due to stocking too much.""",
            },
        },
    }
    please_respond = "Please, answer the question."
    player = "Player"

    # Questionnaire
    questionnaire_age = "What is your age?"

    questionnaire_gender = "What is your gender?"
    questionnaire_gender_male = "Male"
    questionnaire_gender_female = "Female"

    questionnaire_educationLevel = "What level of education have you completed?"
    questionnaire_educationLevel_high_school = "High school"
    questionnaire_educationLevel_undergraduate = "Undergraduate"
    questionnaire_educationLevel_masters = "Masters"
    questionnaire_educationLevel_doctorate = "Doctorate"
    questionnaire_educationLevel_no_high_school = "I have not completed high school"

    questionnaire_employmentStatus = "What is your current employment status?"
    questionnaire_employmentStatus_employed = "Employed"
    questionnaire_employmentStatus_unemployed = "Unemployed"
    questionnaire_employmentStatus_student = "Student"
    questionnaire_employmentStatus_retired = "Retired"

    questionnaire_financialStatusIncome = (
        "What is your <b>monthly</b> income before taxes? (€)"
    )

    questionnaire_financialStatusSavings_1 = (
        "Do you feel you are currently able to save money?"
    )
    questionnaire_financialStatusSavings_2 = (
        "On average, how much money do you keep in your <b>checking account</b>? (€)"
    )

    questionnaire_financialStatusDebt_1 = "Did you borrow money in the past twelve (12) months <b>other than for a mortgage</b>?"
    questionnaire_financialStatusDebt_2 = "Approximately how much money did you borrow in the past twelve (12) months other than for a mortgage? (€)"

    questionnaire_confirm_plural = """Your previous answers seem high. Please, confirm by responding again below."""
    questionnaire_confirm_singular = """Your previous answer seems high. Please, confirm by responding again below."""
    questionnaire_stocks = "Stocks"
    questionnaire_mutualFunds = "Mutual Funds"
    questionnaire_bonds = "Bonds"
    questionnaire_savingsAccounts = "Savings Accounts"
    questionnaire_lifeInsurance = "Life Insurance"
    questionnaire_retirementAccount = "Retirement Accounts"
    questionnaire_crypto = "Cryptocurrency"

    questionnaire_invP_1 = "En matière de placements financiers, que préférez-vous ?"

    questionnaire_invP_risky = "Placer l’essentiel de vos économies sur des placements risqués, mais qui peuvent rapporter beaucoup"
    questionnaire_invP_mostly_risky = "Placer une part importante de vos économies sur des placements risqués, mais qui peuvent rapporter beaucoup, et le reste sur des placements sûrs"
    questionnaire_invP_mostly_safe = "Placer une petite partie de vos économies sur des placements risqués, mais qui peuvent rapporter beaucoup, et le reste sur des placements sûrs"
    questionnaire_invP_safe = "Placer toutes vos économies sur des placements sûrs"

    questionnaire_invP_2_assurance = "Assurance vie"
    questionnaire_invP_2_logement = "Épargne logement"
    questionnaire_invP_2_livret = "Livrets d’épargne"
    questionnaire_invP_2_fonds = "Fonds communs de placement"
    questionnaire_invP_2_actions = "Actions"

    questionnaire_invP_3 = (
        "Imagine you receive 500.000€, what would you do with this money?"
    )
    questionnaire_invP_3_spend_everything = "Spend it all"

    # Finance
    finK_1 = "ENGLISH: Prenons l’hypothèse que vous ayez déposé 1.000 euros sur un compte épargne ayant un rendement de 2 % par an. Selon vous, au bout de cinq ans, combien détiendrez-vous sur votre compte épargne, si vous n’avez pas touché à votre dépôt initial ?"
    finK_1_choice_1 = "ENGLISH: Moins de 1 100 euros"
    finK_1_choice_2 = "ENGLISH: Exactement 1 100 euros"
    finK_1_choice_3 = "ENGLISH: Plus de 1 100 euros"

    finK_2 = "ENGLISH: Imaginez que le taux d’intérêt auquel est rémunérée votre épargne, placée sur un compte, soit de 1 % et l’inflation de 2 % par an. Selon vous, au bout d’un an, avec l’argent sur ce compte, vous serez en mesure d’acheter ?"
    finK_2_choice_1 = "ENGLISH: Plus qu'aujourd'hui"
    finK_2_choice_2 = "ENGLISH: Autant qu'aujourd'hui"
    finK_2_choice_3 = "ENGLISH: Moins qu'aujourd'hui"

    finK_choice_least_risky = "ENGLISH: Le moins risqué"
    finK_choice_second_least_risky = "ENGLISH: Le deuxième moins risqué"
    finK_choice_second_riskiest = "ENGLISH: Le deuxième plus risqué"
    finK_choice_riskiest = "ENGLISH: Le plus risqué"

    finK_3 = "ENGLISH: Livret d’épargne"
    finK_4 = "ENGLISH: Actions"
    finK_5 = "ENGLISH: Obligations"
    finK_6 = "ENGLISH: SICAV/Fond commun de placement (FCP)"

    finK_7 = (
        "An investment with a high return is likely to be high risk, true or false?"
    )
    finK_8 = "High inflation means that the cost of living is increasing rapidly, true or false?"
    finK_9 = "It is usually possible to reduce the risk of investing in the stock market by buying a wide range of stocks and shares, true or false?"

    finB_1 = "Who is responsible for making day-to-day financial decisions in your household?"
    finB_1_choice_0 = "Me"
    finB_1_choice_1 = "My parents"
    finB_1_choice_2 = "My partner"
    finB_1_choice_3 = "I am not sure"

    finB_2 = "Do you have a bank account?"

    finB_3 = "ENGLISH: À quelle fréquence en vérifiez-vous Did the balance in your compte bancaire ?"
    finB_3_choice_1 = "ENGLISH: Tous les jours"
    finB_3_choice_2 = "ENGLISH: Deux à trois fois par semaine"
    finB_3_choice_3 = "ENGLISH: Une fois par semaine"
    finB_3_choice_4 = "ENGLISH: Tous les quinze jours"
    finB_3_choice_5 = "ENGLISH: Une fois par mois"
    finB_3_choice_6 = "ENGLISH: Rarement (moins d'une fois par mois)"
    finB_3_choice_7 = "ENGLISH: Seulement si j'ai besoin d'une grosse somme"
    finB_3_choice_8 = "ENGLISH: Jamais"
    finB_3_choice_0 = "ENGLISH: Ne souhaite pas répondre"

    finB_4 = "ENGLISH: Savez-vous quel est son solde actuel ?"
    finB_4_choice_1 = "ENGLISH: Oui, mais pas précisément"
    finB_4_choice_2 = "ENGLISH: Oui (à ± 5 %)"
    finB_4_choice_3 = "ENGLISH: Non, je ne sais pas"
    finB_4_choice_0 = "ENGLISH: Ne souhaite pas répondre"

    finB_5 = "Do you regularly maintain a budget?"
    finB_6 = "ENGLISH: Étiez-vous déjà à découvert cette année ?"
    finAtt_1 = (
        "I find it more satisfying to spend money than to save it for the long term"
    )

    # Numeracy
    num_1 = "Out of 1,000 people in a small town 500 are members of a choir. Out of these 500 members in the choir 100 are men. Out of the 500 inhabitants that are not in the choir 300 are men. What is the probability that a randomly drawn man is a member of the choir? ________ (%)"
    num_2a = "Imagine we are throwing a five-sided die 50 times. On average, out of these 50 throws how many times would this five-sided die show an odd number (1, 3 or 5)? ______ out of 50 throws."
    num_2b = "Imagine we are throwing a loaded die (6 sides). The probability that the die shows a 6 is twice as high as the probability of each of the other numbers. On average, out of these 70 throws how many times would the die show the number 6? ________out of 70 throws."
    num_3 = "In a forest 20% of mushrooms are red, 50% brown and 30% white. A red mushroom is poisonous with a probability of 20%. A mushroom that is not red is poisonous with a probability of 5%. What is the probability that a poisonous mushroom in the forest is red? ________ (%)"

    numatt_1 = (
        "On a scale of 1 to 5, how confident are you in your mathematical abilities?"
    )
    numatt_2 = "On a scale of 1 to 5, how confident are you in your financial decision-making abilities?"
    numatt_3 = "On a scale of 1 to 5, how confident are you in your understanding of mathematics? "
    numatt_4 = "On a scale of 1 to 5, how confident are you in your understanding of probability?"
    numatt_5 = "On a scale of 1 to 5, how confident are you in your understanding of economics?"
    numatt_not_confident = "Not confident at all"
    numatt_confident = "Absolutely confident"

    # Inflation
    infK_highest = """To the best of your knowledge, what was the <b>highest</b> annual rate of
    inflation that your country experienced during the last 30 years? (%)"""
    infK_lowest = """o the best of your knowledge, what was the <b>lowest</b> annual rate of
    inflation that France experienced during the
    last 30 years? (%)"""
    infK_12 = """To the best of your knowledge, what was the rate of inflation that France
    experienced <b>over the past twelve months</b> (%)?"""
    infK_current = """What is the <b>current</b> rate of inflation in France? (%)"""
    infK_12_price = """On average, by what percentage would you estimate that prices changed in the
    <b>past twelve months</b> in France? (%)"""
    infK_future = """On average, by what percentage do you estimate that prices <b>current</b>
    increase in France next twelve months? (%)"""
    infCI_1 = "If inflation is 10% a year, and a product currently costs {} €, how much will it cost in one year’s time?"
    infCI_2 = "If inflation is 50% a year, and a product currently costs {} €, how much will it cost in two year’s time?"
    infCI_3 = "If inflation is 3% a year, and a product currently costs {} €, how much will it cost in five year’s time?"
    infCI_4 = "If inflation is 100% a year, and a product currently costs {} €, how much will it cost in five year’s time?"
    inf_more_than = "More than {}"
    inf_less_than = "Less than {}"
    inf_4 = "In the previous 12 months, has your purchasing power increased, decreased, or stayed the same?"
    inf_5 = "In the previous 12 months, has your income increased, decreased, or stayed the same?"
    inf_6 = "By what percentage (%) do you estimate your income changed?"
    inf_7 = "In the next 12 months, do you expect your income to increase, decrease, or stay the same?"
    inf_8 = "By what percentage (%) do you expect your income to change?"

    inf_food = "Did your spending on food change over the previous 12 months?"
    inf_housing = "Did your spending on housing change over the previous 12 months?"
    inf_other = (
        "Did your spending on any other expenses change over the previous 12 months?"
    )
    inf_quantity = """Did the quantity of products you regularly purchase change
      over the previous 12 months?"""
    inf_stock = """Did the stock level in your home of products you regularly purchase change
      over the previous 12 months?"""
    inf_checking = (
        "Did the balance in your checking account change over the previous 12 months?"
    )
    inf_savings = (
        "Did the balance in your savings account change over the previous 12 months?"
    )
    inf_percent = "By what percentage"
    inf_change = {
        "inf_5": {
            1: "By about what percentage do you estimate your income increased? (%)",
            -1: "By about what percentage do you estimate your income decreased? (%)",
        },
        "inf_7": {
            1: "By about what percentage do you expect your income to increase? (%)",
            -1: "By about what percentage do you expect your income to decrease? (%)",
        },
        "inf_food": {
            1: "By about what percentage did your spending on food increase? (%)",
            -1: "By about what percentage did your spending on food decrease? (%)",
        },
        "inf_housing": {
            1: "By about what percentage did your spending on housing increase? (%)",
            -1: "By about what percentage did your spending on housing decrease? (%)",
        },
        "inf_other": {
            1: "By about what percentage did your spending on any other expenses increase? (%)",
            -1: "By about what percentage did your spending on any other expenses decrease? (%)",
        },
        "inf_quantity": {
            1: "By about what percentage did the quantity of products you regularly purchase increase? (%)",
            -1: "By about what percentage did the quantity of products you regularly purchase decrease? (%)",
        },
        "inf_stock": {
            1: """By about what percentage did the stock level in your home of products you regularly purchase increase? (%)""",
            -1: """By about what percentage did the stock level in your home of products you regularly purchase decrease? (%)""",
        },
        "inf_checking": {
            1: "By about what percentage did the balance in your checking account increase? (%)",
            -1: "By about what percentage did the balance in your checking account decrease? (%)",
        },
        "inf_savings": {
            1: "By about what percentage did the balance in your savings account increase? (%)",
            -1: "By about what percentage did the balance in your savings account decrease? (%)",
        },
    }

    inf_9_cheaper = "Substitution of current products you buy with cheaper versions"
    inf_9_lessInflated = (
        "Substitution of current products with products less affected by inflation"
    )
    inf_9_quantity = "The quantity of current products you buy"
    inf_9_stockMaintained = (
        "The size of the stock you maintain of products whose price changes"
    )
    inf_9_leisure = "Spending on leisure activities"
    inf_9_subscription = "The number of subscriptions you have"
    inf_9_insurance = "Investment in life insurance"
    inf_9_realEstate = "Investment in real estate"
    inf_9_livret = "Money in savings accounts"
    inf_9_mutualFunds = "Investment in mutual funds"
    inf_9_stocks = "Investment in stocks"
    inf_9_indexedBonds = "Investment in indexed bonds"
    inf_9_checkingAccount = "Money held in checking accounts"
    inf_9_move = "Move to an apartment with lower rent"
    inf_9_income = "Seek additional sources of income"
    inf_9_job = "Seek a new job"
    inf_9_energy = "Reduce energy consumption"
    inf_9_transportation = "Change mode(s) of transport"
    inf_10 = "Have you made at least one of those adjustments in the past 12 months?"
    inf_11 = "Do you think inflation can be controlled?"
    inf_12 = "In your opinion, who should fix inflation?"
    inf_12_choice_businesses = "Private businesses"
    inf_12_choice_politicians = "Governments"
    inf_12_choice_central_banks = "Central banks"
    inf_12_choice_private_banks = "Private banks"
    inf_12_choice_no_one = "No one"

    # Loss aversion
    toss_coin = "Toss coin"
    dont_toss_coin = "Don't toss coin"

    # BRET
    bret_bomb_collected = "Bomb collected"
    bret_boxes_collected = "Number of boxes collected"
    bret_boxes_remaining = "Number of boxes remaining"
    bret_boxes_to_collect = "Number of boxes to collect"
    bret_results = "Results"
    bret_round_history = "Round history"
    bret_round_number = "Round no."
    bret_round_payoff = "Round payoff"
    bret_solve = "Solve"
    bret_start = "Start"
    bret_stop = "Stop"
    bret_your_decision = "Your decision"

    # timePreferences
    timePreferences_task_name = "Payment Scheduler"
    timePreferences_sooner = "Right Now"
    timePreferences_which = "Which do you prefer?"
    timePreferences_delay_1 = "1 week"
    timePreferences_delay_2 = "2 weeks"
    timePreferences_delay_3 = "1 month"
    timePreferences_delay_4 = "3 months"
    timePreferences_delay_5 = "6 months"
    timePreferences_delay_6 = "1 year"

    # sessionResults
    time_preferences = timePreferences_task_name
    loss_aversion = "Lottery with loss"
    risk_preferences = "Lottery"
    wisconsin = "Card game"
    session_results_q1 = """Did you easily understand how to play the game?"""

    session_results_q1_0 = """Yes, by the start of the first game"""

    session_results_q1_1 = """Not entirely at the start of the first game, 
    but I did by the end of it"""

    session_results_q1_2 = """I only understood by the second game"""

    session_results_q1_3 = """I only understood by the third game"""

    session_results_q1_4 = """I only understood by the fourth game"""

    session_results_q1_5 = """I did not really understand"""

    session_results_q2 = """Do you have suggestions to improve the instructions?"""

    session_results_q3 = """Did you appreciate the experiment? Thank you 
    for leaving any further comments you might like to make."""

    session_results_q4 = """Would you be available to be contacted by phone 
    in the near future to discuss your impressions of the experiment for 15 
    minutes? This would include an additional remuneration of %€."""

    session_results_q5 = """Did you find the explanation of the optimal
    strategy clear?"""

    session_results_q6 = """Do you think that the explanation of the 
    optimal strategy helped you play the game better?"""

    # Error messages
    error_questionnaire_message_age = (
        "You must be 18 years of age or older to participate."
    )
    error_questionnaire_message_a1 = "Please enter a valid age in years."
    error_task_insufficient_cash = (
        f"Your do not have sufficient {total_cash} to complete this purchase."
    )
    error_task_instructions_general = (
        "That is incorrect. Please, review the instructions and correct your answer."
    )
    error_task_instructions_q3 = f"""That is incorrect. The {interest_rate} 
    (%) does not change. The {interest_earned_last_period} may vary based on 
    the amount in your {savings_account} when you end a month."""

    error_task_instructions_q4 = f"""That is incorrect. Note that {total_cash} 
    = {savings_account} (from previous month) + {interest_earned_last_period} 
    + Monthly Salary."""

    error_task_instructions_q7 = (
        "You have not placed the slider on {}%. Try adjusting the slider again."
    )
    error_task_instructions_q8 = """The {} in {} is not {} units of {}. Please, 
    review the instructions and adjust the {} in {}."""

    error_task_instructions_q9 = """The value of {} is not {}. Please, review 
    the instructions. Adjust the {} in {} while paying attention to the value in {}."""

    error_task_instructions_q10 = """Your {} does not have {} unit. Please try 
    adjusting the {} in {} while paying attention to the value in {}."""

    error_task_instructions_q11 = """That is incorrect. The price 
    can change, but it cannot decrease."""

    error_finance_finK_3_6 = "Please, ensure you have distinguished between each product from 1 to 4 (from the least risky to the riskiest)."
    error_not_correct_selection = (
        "That is not the correct selection. Please, try again."
    )

    error_task_int_intro_1 = """That is incorrect. The price changed by ({} - {}) ÷ {} = {}%. The interest rate is {}%."""

    error_task_int_q1 = f"""That is incorrect. If {interest_rate} is 
    less than {inflation_rate}, you can buy less."""

    error_task_int_q2 = f"""That is incorrect. If {interest_rate} is 
    less than {inflation_rate} and you have 0 {food} in {stock}, 
    you should stock up."""

    error_task_int_q3 = f"""That is incorrect. If {interest_rate} is 
    greater than {inflation_rate}, you can buy more."""

    error_task_int_q4 = f"""That is incorrect. If {interest_rate} is 
    greater than {inflation_rate} and you have {food} in {stock}, 
    you should not buy any {food}."""

    error_task_int_q5 = f"""That is incorrect. If {interest_rate} is 
    greater than {inflation_rate},  you can buy more."""

    error_task_int_q6 = f"""That is incorrect. If {interest_rate} is 
    greater than {inflation_rate} and you have 0 {units} of {food}, 
    you should buy 1 {unit}."""

    error_task_int_q7 = f"""That is incorrect. If {interest_rate} is 
    less than {inflation_rate}, you can buy less."""

    error_task_int_q8 = f"""That is incorrect. If {interest_rate} is 
    less than {inflation_rate}, you expect that will last 4 months, and you 
    have 0 {units} of {food}, you should buy a quantity equal to the 
    number of months you expect {inflation_rate} to remain greater than 
    {interest_rate}."""
