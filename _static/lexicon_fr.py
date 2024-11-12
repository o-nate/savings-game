from settings import SESSION_CONFIG_DEFAULTS


class Lexicon:
    """Define French terms here"""

    # task
    starting_balances = "Soldes de Départ"
    interest_earned_last_period = "Intérêts Perçus le Mois Précédent"
    total_cash = "Encaisse Totale"
    ending_balances = "Soldes de Clôture"
    savings_account = "Compte Épargne"
    stock = "Stock"
    unit = "unité"
    units = "unités"
    market_data = "Données du Marché"
    salary = "Salaire"
    catalog = "Catalogue"
    food = "Aliments"
    price = "Prix"
    my_cart = "Mon Panier"
    name = "Nom"
    quantity = "Quantité"
    prix_total = "Prix Total"
    finalize_purchase = "Finaliser l’Achat"
    total = "Total"
    slider_your_value = "Votre estimation"
    cancel = "Annuler"

    warning_final_purch = """ATTENTION VOUS N'ALLEZ PAS SURVIVRE !! 
    • Le solde de votre stock est actuellement de 0.
    • Si c'est une erreur, veuillez cliquer sur *Annuler* et mettre à jour votre panier. 
    • Si vous n'avez pas assez d'argent, veuillez cliquer sur *OK* pour terminer le jeu et passer aux tâches supplémentaires."""

    warning_final_purch_2 = """****Êtes-vous sûr(e) de ne pas vouloir survivre ?****
    • Cliquez sur "Annuler" pour changer votre panier.
    • Cliquez sur "OK" si vous voulez ne pas survivre."""

    qualitative_estimate = (
        """Trouvez‑vous que, au cours des douze derniers mois, les prix ont..."""
    )

    qualitative_expectation_month_1 = """Quelle sera à votre avis l’évolution 
    des prix au cours des douze prochains mois ?"""

    qualitative_expectation = """Par rapport aux douze derniers mois, quelle 
        sera à votre avis l’évolution des prix au cours des douze prochains mois ?"""

    qualitative_est_rapid = "Fortement augmenté"
    qualitative_est_moderate = "Moyennement augmenté"
    qualitative_est_slight = "Un peu augmenté"
    qualitative_est_same = "Stagné"
    qualitative_est_decrease = "Diminué"

    ## For month 1
    qualitative_exp_rapid_month_1 = "Elle va être rapide"
    qualitative_exp_moderate_month_1 = "Elle va se poursuivre moyennement"
    qualitative_exp_slight_month_1 = "Elle va être lente"
    qualitative_exp_same_month_1 = "Les prix vont rester stationnaires"
    qualitative_exp_decrease_month_1 = "Les prix vont diminuer"

    qualitative_exp_rapid = "Elle va être plus rapide"
    qualitative_exp_moderate = "Elle va se poursuivre au même rythme"
    qualitative_exp_slight = "Elle va être moins rapide"
    qualitative_exp_same = "Les prix vont rester stationnaires"
    qualitative_exp_decrease = "Les prix vont diminuer"

    inf_estimate = """De quel pourcentage pensez‑vous que les prix ont 
    augmenté (ou baissé) au cours des douze derniers mois ? (donner une valeur en %)."""

    inf_expectation = """De quel pourcentage pensez‑vous que les prix vont 
    augmenter (ou baisser) au cours des douze prochains mois ? (donner une valeur en %)"""

    slider = "Curseur"

    # General terms
    game = "Jeu de l'Épargne"
    I_do_not_know = "Je ne sais pas"
    yes = "Oui"
    no = "Non"
    maybe = "Peut-être"
    somewhat = "En partie"
    true = "Vrai"
    false = "Faux"
    not_applicable = "Pas concerné"
    more = "Plus"
    less = "Moins"
    the_same_amount = "La même quantité"
    more_money = "Plus d'argent"
    less_money = "Moins d'argent"
    same_money = "Autant d'argent"
    nothing = "Rien"
    none_of_the_above = "Aucun de ces éléments"
    next = "Suivant"

    click_next = """Cliquez sur le bouton "Suivant" ci-dessous 
    lorsque vous serez prêt à poursuivre."""
    round = "{} tour"
    first_round = "premier tour"
    last_round = "dernier tour"
    second = "ème"
    third = "ème"
    nth = "ème"

    completed_questionnaire = """Vous avez maintenant terminé le 
    questionnaire. Cliquez sur le bouton "Suivant" ci-dessous 
    lorsque vous êtes prêt à continuer."""

    completed_game_round = f"""Vous avez maintenant terminé le 
    tour du jeu d’aujourd’hui. {click_next}"""

    completed_task_round = f"""Vous avez maintenant terminé le 
    tour du jeu d’aujourd’hui et les questions de suivi. 
    <br><br>{click_next}"""

    sliders_instructions = f"""Cliquez sur la barre bleue pour 
    faire apparaître le {slider}. Faîtes-le glisser le long 
    de la barre pour sélectionner votre estimation avec votre souris 
    ou les flèches de votre clavier."""

    remunerated_questions = "Questions rémunérées"
    increased = "Augmenté"
    decreased = "Baissé"
    stayed_same = "Resté constant"
    increase = "Augmente"
    decrease = "Baisse"
    stay_same = "Reste constant"
    no_change = "Pas de changement"
    it_increases = "Il augmente."
    it_decreases = "Il baisse."
    it_stays_the_same = "Il reste constant."
    not_enough_info = "Il n'y a pas assez d'informations pour déterminer l'effet."
    instructions = "Instructions"
    correct = "C'est exact."
    interest_rate = "Taux d'Intérêt"
    nominal_interest_rate = "Taux d'Intérêt Nominal"
    real_interest_rate = "Taux d'Intérêt Réel"
    inflation_rate = "Taux d'Inflation"
    purchasing_power = "Pouvoir d'Achat"
    completed_so_far = "État d'avancement"
    comprehension = "Compréhension"
    stock_up = f"Acheter plus d'une {unit}"
    save = f"Acheter 0 {unit}"
    buy_1 = f"Acheter 1 {unit}"
    buy_x = "Acheter {} {}"
    buy_more_than = "Acheter plus de {} {}"

    # init
    wait_for_next_button = """Le bouton "Suivant" va apparaître bientôt"""
    redirected = "Vous allez être redirigée vers la page de l'expérience."

    # redirectapp
    important_reminder = "Rappel important :"
    please_wait = "Veuillez patienter..."
    session_tomorrow = "La session suivante aura lieu demain."
    thank_you_for_participation = (
        "Merci pour votre participation à la session de cette journée."
    )
    continue_button = "Continuer"

    # task_instructions
    description_months = f"""Vous voyez ici combien de mois 
    virtuels à jouer. Chaque jeu dure {SESSION_CONFIG_DEFAULTS['task_duration']} 
    mois virtuels au total."""

    description_interest_earned_last_period = f"""Il indique le 
    montant des intérêts perçus sur votre {savings_account} au cours 
    du mois virtuel précédent."""

    description_total_cash = f"""L'{total_cash} est le montant 
    à dépenser pour les {units} d'{food} chaque mois, ou à épargner chaque 
    mois."""

    description_savings_account = f"""Il s'agit du montant que 
    vous conserverez pour le mois suivant après avoir cliqué sur 
    {finalize_purchase} en bas de la page. Il s'agit également du 
    montant sur lequel vous percevrez des intérêts."""

    description_stock = f"""Ici, vous voyez combien d’{units} 
    d’{food} vous avez dans votre {stock}."""

    description_interest_rate = f"""Le pourcentage du total de 
    votre {savings_account} qui sera ajouté le mois prochain. Ce 
    taux ne change pas pendant le jeu."""

    description_salary = """Un montant supplémentaire de monnaie du jeu que vous 
    recevez chaque mois. Ce montant ne change pas au cours du jeu."""

    description_catalog = f"""Le {catalog} affiche le prix 
    actuel d’une {unit} d’{food}. Pour ajouter des 
    {units} d'{food} à {my_cart}, cliquez sur le bouton 
    gris +1 autant de fois que nécessaire."""

    description_my_cart = f"""{my_cart} vous indique la 
    quantité d’unités d'Aliments que vous avez sélectionnée et le 
    prix total que vous allez payer pour cette quantité."""

    q1 = "Sélectionnez : Votre rémunération est basée sur la valeur finale de …"

    q2 = f"""Quel est le nombre minimum d’{unit} d’{food} 
    que vous devez avoir dans votre {stock} avant de cliquer sur 
    le bouton "{finalize_purchase}" pour survivre au mois 
    suivant ?"""

    q3 = f"Le {interest_rate} peut-il changer pendant le jeu ?"

    q4 = f"""Supposons qu'un joueur avait 100₮ sur son 
    {savings_account} le mois dernier. S'il gagne 10₮ d'intérêts 
    et reçoit 20₮ de salaire mensuel, quel sera le montant total de 
    son {total_cash} ?"""

    q11 = f"""Le prix d'une {unit} d'{food} peut-il changer ?"""

    q1_choice_4 = "Intérêts perçus"
    q3_choice_3 = f"Cela dépend du montant du {savings_account}"
    q3_choice_4 = f"Cela dépend du montant de l’{total_cash}"
    q4_choice_5 = "Nous ne disposons pas d'informations suffisantes pour le déterminer."
    q11_choice_1 = "Il peut augmenter et baisser"
    q11_choice_2 = "Il ne peut qu'augmenter"
    q11_choice_3 = "Il ne peut que baisser"
    q11_choice_4 = "Il ne peut pas changer"

    # task_questions
    priceMemory = "Quel était le prix le mois"

    # task_int
    task_int_test_completed = """Félicitations, vous avez réussi le test de 
    compréhension. Nous allons maintenant commencer le jeu à nouveau."""

    task_int_intro_1 = f"""Le {inflation_rate} est déterminé par :"""
    task_int_intro_1_rising_price = f"La hausse du prix des {food}"
    task_int_intro_1_rising_interest = f"La hausse du {salary}"
    task_int_intro_1_rising_salary = f"La hausse du {salary}"

    task_int_q_qt = f"""Pourrez-vous acheter plus, moins, ou la 
    même quantité d'{food} qu'avant ?"""

    task_int_q_do = "Que devez-vous faire dans la situation présentée ci-dessous ?"

    task_int_high_inf = "Inflation plus forte"
    task_int_low_inf = "Inflation plus faible"

    task_int_explain = {
        "early": {
            3: {
                "true": """C'est exact. Il est important de résister à l'envie de constituer des stocks trop tôt et de sacrifier ainsi les intérêts pouvant être gagnés. À l'avenir, vérifiez si vous êtes confronté à une inflation forte ou faible avant de constituer des stocks.""",
                "false": """Vous n'avez supporté aucun coût dû à un stockage trop précoce.""",
            },
            2: {
                "true": """C'est exact. Vous n’avez supporté aucun coût en raison d'un stockage trop précoce.""",
                "false": """Vous avez bien supporté un coût dû à un stockage trop précoce. Il est important de résister à l'envie de constituer des stocks trop tôt et de sacrifier ainsi les intérêts pouvant être gagnés. À l'avenir, vérifiez si vous êtes confronté à une inflation forte ou faible avant de constituer des stocks.""",
            },
            0: {
                "true": """Vous avez bien supporté un coût dû à un stockage trop précoce. Il est important de résister à l'envie de constituer des stocks trop tôt et de sacrifier ainsi les intérêts pouvant être gagnés. À l'avenir, vérifiez si vous êtes confronté à une inflation forte ou faible avant de constituer des stocks.""",
                "false": """Vous n'avez supporté aucun coût dû à un stockage trop précoce. Il est important de résister à l'envie de constituer des stocks trop tôt et de sacrifier ainsi les intérêts pouvant être gagnés. À l'avenir, vérifiez si vous êtes confronté à une inflation forte ou faible avant de constituer des stocks.""",
            },
        },
        "late": {
            3: {
                "true": """C'est exact. Il est important de stocker rapidement lorsque l’inflation augmente fortement. Il est important de faire attention aux prix pour vérifier si vous êtes confronté à une inflation forte ou faible.""",
                "false": """Vous n'avez supporté aucun coût en raison d'un stock insuffisant ou trop tardif.""",
            },
            2: {
                "true": """C'est exact. Vous n'avez supporté aucun coût en raison d'un stock insuffisant ou trop tardif.""",
                "false": """Vous avez bien supporté un coût en raison d'un stock insuffisant ou trop tardif. Il est important de stocker rapidement lorsque l’inflation augmente fortement. N'oubliez pas de faire attention aux prix pour vérifier si vous êtes confronté à une inflation forte ou faible.""",
            },
            0: {
                "true": """Vous avez bien supporté un coût en raison d'un stock insuffisant ou trop tardif. Il est important de stocker rapidement lorsque l’inflation augmente fortement. N'oubliez pas de faire attention aux prix pour vérifier si vous êtes confronté à une inflation forte ou faible.""",
                "false": """Vous n'avez supporté aucun coût en raison d'un stock insuffisant ou trop tardif.""",
            },
        },
        "excess": {
            3: {
                "true": """C'est exact. Il est important de faire attention à la quantité de biens nécessaire pour survivre jusqu’à la fin du jeu. Votre stock ne doit jamais être supérieur à cette quantité.""",
                "false": """Vous n’avez supporté aucun coût en raison d’un excès de stockage.""",
            },
            2: {
                "true": """C'est exact. Vous n’avez supporté aucun coût en raison d’un excès de stockage.""",
                "false": """Vous avez bien supporté un coût en raison d’un excès de stockage. Il est important de faire attention à la quantité de biens nécessaire pour survivre jusqu’à la fin du jeu. Votre stock ne doit jamais être supérieur à cette quantité.""",
            },
            0: {
                "true": """Vous avez bien supporté un coût en raison d’un excès de stockage. Il est important de faire attention à la quantité de biens nécessaire pour survivre jusqu’à la fin du jeu. Votre stock ne doit jamais être supérieur à cette quantité.""",
                "false": """Vous n’avez supporté aucun coût en raison d’un excès de stockage.""",
            },
        },
    }
    please_respond = "Veuillez répondre à la question"
    player = "Joueur"

    # Questionnaire
    questionnaire_age = "Quel est votre âge ?"

    questionnaire_gender = "Quel est votre sexe ?"
    questionnaire_gender_male = "Homme"
    questionnaire_gender_female = "Femme"

    questionnaire_educationLevel = "Quel est votre niveau d'études ?"
    questionnaire_educationLevel_high_school = "Baccalauréat"
    questionnaire_educationLevel_undergraduate = "Premier cycle universitaire"
    questionnaire_educationLevel_masters = "Master"
    questionnaire_educationLevel_doctorate = "Doctorat"
    questionnaire_educationLevel_no_high_school = (
        "Je n'ai pas terminé mes études secondaires"
    )

    questionnaire_employmentStatus = (
        "Quelle est votre situation professionnelle actuelle ?"
    )
    questionnaire_employmentStatus_employed = (
        "En emploi (salarié ou travailleur indépendant)"
    )
    questionnaire_employmentStatus_unemployed = "Chômeur"
    questionnaire_employmentStatus_student = "Étudiant"
    questionnaire_employmentStatus_retired = "Retraité"

    questionnaire_financialStatusIncome = (
        "Quel est votre revenu <b>mensuel</b> avant le règlement des impôts ? (€)"
    )

    questionnaire_financialStatusSavings_1 = "Pensez-vous être en mesure d’épargner?"
    questionnaire_financialStatusSavings_2 = (
        "En moyenne, quelle somme  gardez-vous sur votre <b>compte courant</b> ? (€)"
    )

    questionnaire_financialStatusDebt_1 = "Avez-vous emprunté de l'argent au cours des douze (12) derniers mois, autrement que pour un emprunt immobilier ?"
    questionnaire_financialStatusDebt_2 = "Quelle somme (environ) avez-vous emprunté au cours des douze (12) derniers mois, <b>autrement que pour un emprunt immobilier</b> ? (€)"
    questionnaire_confirm_plural = """Vos réponses précédentes semblent élévées. Veuillez confirmer en répondant à nouveau ci-dessous."""
    questionnaire_confirm_singular = """Votre réponse précédente semble élévée. Veuillez confirmer en répondant à nouveau ci-dessous."""
    questionnaire_stocks = "Actions"
    questionnaire_mutualFunds = "SICAV ou Fonds communs de placement"
    questionnaire_bonds = "Obligations"
    questionnaire_savingsAccounts = "Comptes, plans ou livrets d'épargne"
    questionnaire_lifeInsurance = "Assurance vie"
    questionnaire_retirementAccount = "Comptes épargne retraite"
    questionnaire_crypto = "Crypto-monnaies"

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
        "Imaginez que vous recevez 500.000€. Que faites-vous avec cet argent ?"
    )
    questionnaire_invP_3_spend_everything = "Dépenser tout"

    # Finance
    finK_1 = "Prenons l’hypothèse que vous ayez déposé 1.000 euros sur un compte épargne ayant un rendement de 2 % par an. Selon vous, au bout de cinq ans, combien détiendrez-vous sur votre compte épargne, si vous n’avez pas touché à votre dépôt initial ?"
    finK_1_choice_1 = "Moins de 1 100 euros"
    finK_1_choice_2 = "Exactement 1 100 euros"
    finK_1_choice_3 = "Plus de 1 100 euros"

    finK_2 = "Imaginez que le taux d’intérêt auquel est rémunérée votre épargne, placée sur un compte, soit de 1 % et l’inflation de 2 % par an. Selon vous, au bout d’un an, avec l’argent sur ce compte, vous serez en mesure d’acheter ?"
    finK_2_choice_1 = "Plus qu'aujourd'hui"
    finK_2_choice_2 = "Autant qu'aujourd'hui"
    finK_2_choice_3 = "Moins qu'aujourd'hui"

    finK_choice_least_risky = "Le moins risqué"
    finK_choice_second_least_risky = "Le deuxième moins risqué"
    finK_choice_second_riskiest = "Le deuxième plus risqué"
    finK_choice_riskiest = "Le plus risqué"

    finK_3 = "Livret d’épargne"
    finK_4 = "Actions"
    finK_5 = "Obligations"
    finK_6 = "SICAV/Fond commun de placement (FCP)"

    finK_7 = "Un investissement avec un rendement élevé est susceptible de comporter un risque élevé, vrai ou faux ?"
    finK_8 = "Une inflation élevée signifie que le coût de la vie augmente rapidement, vrai ou faux ?"
    finK_9 = "Il est généralement possible de réduire le risque d'investir en bourse en achetant un large éventail d'actions et de parts, vrai ou faux ?"

    finB_1 = "Qui est chargé de prendre les décisions financières quotidiennes dans votre foyer ?"
    finB_1_choice_0 = "Moi"
    finB_1_choice_1 = "Mes parents"
    finB_1_choice_2 = "Mon partenaire"
    finB_1_choice_3 = "Cela dépend"

    finB_2 = "Avez-vous un compte bancaire ?"

    finB_3 = "À quelle fréquence vérifiez-vous le solde de votre compte bancaire ?"
    finB_3_choice_1 = "Tous les jours"
    finB_3_choice_2 = "Deux à trois fois par semaine"
    finB_3_choice_3 = "Une fois par semaine"
    finB_3_choice_4 = "Tous les quinze jours"
    finB_3_choice_5 = "Une fois par mois"
    finB_3_choice_6 = "Rarement (moins d'une fois par mois)"
    finB_3_choice_7 = "Seulement si j'ai besoin d'une grosse somme"
    finB_3_choice_8 = "Jamais"
    finB_3_choice_0 = "Ne souhaite pas répondre"

    finB_4 = "Savez-vous quel est son solde actuel ?"
    finB_4_choice_1 = "Oui, mais pas précisément"
    finB_4_choice_2 = "Oui (à ± 5 %)"
    finB_4_choice_3 = "Non, je ne sais pas"
    finB_4_choice_0 = "Ne souhaite pas répondre"

    finB_5 = "Faites-vous vos comptes régulièrement ?"
    finB_6 = "Avez-vous déjà été à découvert cette année ?"
    finAtt_1 = "Je trouve plus satisfaisant de dépenser de l'argent que de l'économiser à long terme."

    # Numeracy
    num_1 = """Sur les 1.000 habitants d'une petite ville, 500 sont membres 
    d'une chorale. Sur ces 500 membres de la chorale, 100 sont des hommes. Sur 
    les 500 habitants qui ne sont pas dans la chorale, 300 sont des hommes. 
    Quelle est le pourcentage de chance qu'un homme tiré au hasard soit membre 
    de la chorale ? ________ (%) <br><br> (Indiquez un nombre entier)"""

    num_2a = "Imaginez que nous lançons 50 fois un dé à cinq faces. En moyenne, sur ces 50 lancers, combien de fois ce dé à cinq faces indiquera-t-il un nombre impair (1, 3 ou 5) ? ______ sur 50 lancers."
    num_2b = "Imaginez que nous lançons un dé pipé (6 faces). Le pourcentage de chance que le dé indique un 6 est deux fois plus élevée que la probabilité de chacun des autres chiffres. En moyenne, sur ces 70 lancers, combien de fois le dé affichera-t-il le chiffre 6 ? ________ sur 70 lancers."
    num_3 = "Dans une forêt, 20% des champignons sont rouges, 50% bruns et 30% blancs. Un champignon rouge est toxique avec un pourcentage de chance de 20%. Un champignon qui n'est pas rouge est toxique avec un pourcentage de chance de 5 %. Quelle est le pourcentage de chance qu'un champignon toxique de la forêt soit rouge ? ________ (%)"

    numatt_1 = "Sur une échelle de 1 à 5, quel est votre degré de confiance dans vos capacités mathématiques ?"
    numatt_2 = "Sur une échelle de 1 à 5, quel est votre degré de confiance dans vos capacités à prendre des décisions financières ?"
    numatt_3 = "Sur une échelle de 1 à 5, quel est votre degré de confiance dans votre compréhension des probabilités ?"
    numatt_4 = "Sur une échelle de 1 à 5, quel est votre degré de confiance dans votre compréhension de l'économie ?"
    numatt_not_confident = "Pas du tout confiant"
    numatt_confident = "Absolument confiant"

    # Inflation
    infK_highest = """À votre connaissance, quel est le taux d'inflation annuel le <b>plus
    élevé</b> que la France a connu au cours des 30 dernières années ? (%)"""
    infK_lowest = """À votre connaissance, quel est le taux d'inflation annuel le <b>plus bas</b>
    que la France a connu au cours des 30 dernières années ? (%)"""
    infK_12 = """À votre connaissance, quel est le taux d'inflation que la France a connu au
    cours des <b>douze derniers mois</b> ? (%)"""
    infK_current = """Quel est le taux d'inflation <b>actuel</b> en France ? (%)"""
    infK_12_price = """En moyenne, de quel pourcentage estimez-vous que les prix ont changé au cours
    des <b>douze derniers mois</b> en
    France ? (%)"""
    infK_future = """En moyenne, de quel pourcentage estimez-vous que les prix <b>vont
        augmenter</b> en France au cours des douze
    prochains mois ? (%)"""
    infCI_1 = "Si l'inflation est de 10% par an, et qu'un produit coûte actuellement {} €, combien coûtera-t-il dans un an ?"
    infCI_2 = "Si l'inflation est de 50% par an, et qu'un produit coûte actuellement {} €, combien coûtera-t-il dans deux ans ?"
    infCI_3 = "Si l'inflation est de 3% par an, et qu'un produit coûte actuellement {} €, combien coûtera-t-il dans cinq ans ?"
    infCI_4 = "Si l'inflation est de 100% par an, et qu'un produit coûte actuellement {} €, combien coûtera-t-il dans cinq ans ?"
    inf_more_than = "Plus de {} €"
    inf_less_than = "Moins de {} €"
    inf_4 = "Votre pouvoir d’achat a-t-il augmenté, baissé, resté constant pendant les 12 derniers mois ?"
    inf_5 = "Votre revenu a-t-il été augmenté, baissé, resté constant pendant les 12 derniers mois ?"
    inf_6 = "De quel pourcentage (%) estimez-vous que votre revenu a changé ?"
    inf_7 = "Vous attendez-vous à ce que votre revenu augmente, baisse, ou reste constant dans les 12 prochains mois ?"
    inf_8 = "De quel pourcentage (%) vous attendez une augmentation ou une baisse de votre revenu cette année ?"
    inf_food = (
        "Vos dépenses d’alimentation ont-elles varié au cours des 12 derniers mois ?"
    )
    inf_housing = (
        "Vos dépenses d’immobilier ont-elles varié au cours des 12 derniers mois ?"
    )
    inf_other = "Vos autres dépenses ont-elles varié au cours des 12 derniers mois ?"
    inf_quantity = """La quantité de produits achetés régulièrement a-t-elle
      varié au cours des 12 derniers mois ?"""
    inf_stock = """Le niveau de stock maintenu chez vous de produits achetés
      régulièrement a-t-il varié au cours des 12 derniers mois ?"""
    inf_balance_change = (
        "Le solde de votre {} a-t-il varié au cours des 12 derniers mois ?"
    )
    inf_checking = (
        "Le solde de votre compte courrant a-t-il varié au cours des 12 derniers mois ?"
    )
    inf_savings = (
        "Le solde de votre compte épargne a-t-il varié au cours des 12 derniers mois ?"
    )
    inf_percent = "De quel pourcentage"
    inf_change = {
        "inf_5": {
            1: "De quel pourcentage environ estimez-vous que votre revenu a augmenté ? (%)",
            -1: "De quel pourcentage environ estimez-vous que votre revenu a baissé ? (%)",
        },
        "inf_7": {
            1: "De quel pourcentage environ vous attendez une augmentation de votre revenu cette année ? (%)",
            -1: "De quel pourcentage environ vous attendez une baisse de votre revenu cette année ? (%)",
        },
        "inf_food": {
            1: "De quel pourcentage environ vos dépenses d'alimention ont-elles augmenté ? (%)",
            -1: "De quel pourcentage environ vos dépenses d'alimention ont-elles baissé ? (%)",
        },
        "inf_housing": {
            1: "De quel pourcentage environ vos dépenses d’immobilier ont-elles augmenté ? (%)",
            -1: "De quel pourcentage environ vos dépenses d’immobilier ont-elles baissé ? (%)",
        },
        "inf_other": {
            1: "De quel pourcentage environ vos autres dépenses ont-elles augmenté ? (%)",
            -1: "De quel pourcentage environ vos autres dépenses ont-elles baissé ? (%)",
        },
        "inf_quantity": {
            1: "De quel pourcentage environ la quantité de produits achetés régulièrement a-t-elle augmenté ? (%)",
            -1: "De quel pourcentage environ la quantité de produits achetés régulièrement a-t-elle baissé ? (%)",
        },
        "inf_stock": {
            1: """De quel pourcentage environ le niveau de stock maintenu chez vous de produits achetés régulièrement a-t-il augmenté ? (%)""",
            -1: """De quel pourcentage environ le niveau de stock maintenu chez vous de produits achetés régulièrement a-t-il baissé ? (%)""",
        },
        "inf_checking": {
            1: "De quel pourcentage environ le solde de votre compte courrant a-t-il augmenté ? (%)",
            -1: "De quel pourcentage environ le solde de votre compte courrant a-t-il baissé ? (%)",
        },
        "inf_savings": {
            1: "De quel pourcentage environ le solde de votre compte épargne a-t-il augmenté ? (%)",
            -1: "De quel pourcentage environ le solde de votre compte épargne a-t-il baissé ? (%)",
        },
    }

    inf_9_cheaper = "Substitution des produits actuels que vous achetez par des produits moins chers"
    inf_9_lessInflated = (
        "Substitution des produits actuels par des produits moins soumis à l'inflation"
    )
    inf_9_quantity = "La quantité de produits courants que vous achetez"
    inf_9_stockMaintained = (
        "La taille du stock que vous détenez de produits dont le prix change"
    )
    inf_9_leisure = "Dépenses pour les activités de loisirs"
    inf_9_subscription = "Le nombre des abonnements"
    inf_9_insurance = "Placement dans l'assurance-vie"
    inf_9_realEstate = "Placement dans l'immobilier"
    inf_9_livret = "Placement dans des comptes d'épargne"
    inf_9_mutualFunds = "Placement dans des fonds communs de placement"
    inf_9_stocks = "Placement en actions"
    inf_9_indexedBonds = "Placement dans des obligations indexées sur l'inflation"
    inf_9_checkingAccount = "Placement dans des comptes courants"
    inf_9_move = "Déménager dans un appartement dont le loyer est moins élevé"
    inf_9_income = "Rechercher des sources de revenus supplémentaires"
    inf_9_job = "Chercher un nouvel emploi"
    inf_9_energy = "Investir pour réduire votre consommation d'énergie"
    inf_9_transportation = "Modifier vos déplacements"
    inf_10 = (
        "Avez-vous fait au moins un de ces ajustements au cours des 12 derniers mois ?"
    )
    inf_11 = "Pensez-vous que l'inflation peut être contrôlée ?"
    inf_12 = "À votre avis, qui devrait contrôler l'inflation ?"
    inf_12_choice_businesses = "Entreprises privées"
    inf_12_choice_politicians = "Gouvernements"
    inf_12_choice_central_banks = "Banques centrales"
    inf_12_choice_private_banks = "Banques privées"
    inf_12_choice_no_one = "Personne"

    # Loss aversion
    toss_coin = "Lancer la pièce"
    dont_toss_coin = "Ne pas lancer"

    # BRET
    bret_bomb_collected = "Bombe collectée"
    bret_boxes_collected = "Nombre de boîtes collectées"
    bret_boxes_remaining = "Number of boxes remaining"
    bret_boxes_to_collect = "Nombre de boîtes restantes"
    bret_results = "Résultats"
    bret_round_history = "Histoire des tours"
    bret_round_number = "Numéro du tour"
    bret_round_payoff = "Gain du tour"
    bret_start = "Début"
    bret_stop = "Stop"
    bret_solve = "Résoudre"
    bret_your_decision = "Votre décision"

    # timePreferences
    timePreferences_task_name = "Planificateur de paiement"
    timePreferences_sooner = "Maintenant"
    timePreferences_which = "Que préférez-vous ?"
    timePreferences_delay_1 = "1 semaine"
    timePreferences_delay_2 = "2 semaines"
    timePreferences_delay_3 = "1 mois"
    timePreferences_delay_4 = "3 mois"
    timePreferences_delay_5 = "6 mois"
    timePreferences_delay_6 = "1 an"

    # sessionResults
    time_preferences = timePreferences_task_name
    loss_aversion = "Loterie avec perte"
    risk_preferences = "Loterie"
    wisconsin = "Jeu des cartes"
    session_results_q1 = """Avez-vous compris facilement comment jouer au 
    jeu ?"""

    session_results_q1_0 = """Oui, dès le début du premier jeu"""

    session_results_q1_1 = """Un peu difficilement au début du premier jeu, 
    mais c'était mieux à la fin"""

    session_results_q1_2 = """Je n'ai compris que la deuxième fois"""

    session_results_q1_3 = """Je n'ai compris que la troisième fois"""

    session_results_q1_4 = """Je n'ai compris que la quatrième fois"""

    session_results_q1_5 = """Je n'ai pas vraiment compris"""

    session_results_q2 = """Avez-vous de commentaires à faire pour 
    améliorer les instructions de l'expérience ?"""

    session_results_q3 = """Avez-vous apprécié l'expérience ? Merci de nous 
    laisser des commentaires si vous le souhaitez"""

    session_results_q4 = """Seriez-vous disponible pour être contacté par 
    téléphone dans le futur proche pour discuter de vos impressions de 
    l'expérience pour 15 minutes ? Cela inclura une indemnité supplémentaire de 
    5€."""

    session_results_q5 = """Avez-vous trouvé l'explication de la stratégie
    optimale claire ?"""

    session_results_q6 = """Pensez-vous que l'explication de la stratégie 
    optimale vous a aidé à mieux jouer le jeu ?"""

    # Error messages
    error_questionnaire_message_age = """Vous devez être âgé de 
    18 ans ou plus pour participer."""

    error_questionnaire_message_a1 = """Veuillez entrer un âge 
    valide en années."""

    error_task_insufficient_cash = f"""Vous n'avez pas assez 
    d'{total_cash} pour finaliser cet achat."""

    error_task_instructions_general = """C'est inexact. Veuillez 
    revoir les instructions et corriger votre réponse."""

    error_task_instructions_q3 = f"""C'est inexact. Le 
    {interest_rate} (%) ne change pas. Les 
    {interest_earned_last_period} peuvent varier en fonction du 
    montant de votre {savings_account} à la fin du mois."""

    error_task_instructions_q4 = f"""C'est inexact. Notez que : 
    {total_cash} = {savings_account} (du mois précédent) + 
    {interest_earned_last_period} + Salaire Mensuel."""

    error_task_instructions_q7 = """Vous n'avez pas placé le 
    curseur sur {}%. Essayez de régler à nouveau le curseur."""

    error_task_instructions_q8 = """La {} dans {} n'est pas {} 
    unités d'{}. Veuillez revoir les instructions et ajuster la {} 
    de {}."""

    error_task_instructions_q9 = """La valeur du {} n'est pas 
    {}. Veuillez revoir les instructions. Ajustez la {} dans {} tout 
    en faisant attention à la valeur du {}."""

    error_task_instructions_q10 = """Votre {} n'est pas d’{} 
    unité. Veuillez essayer d'ajuster la {} dans {} tout en faisant 
    attention à la valeur dans {}."""

    error_task_instructions_q11 = """C'est inexact. Le prix peut 
    changer, mais il ne peut pas baisser."""

    error_finance_finK_3_6 = """Veuillez verifier que vous avez 
    bien distingué les risque de chaque produits de 1 à 4 (du moins 
    risqué au plus risqué)"""

    error_not_correct_selection = "C'est inexact. Veuillez réessayer."

    error_task_int_intro_1 = """C'est inexat. Le prix a changé de ({} - {}) ÷ {} = {}%. Le taux d'intérêt est de {}%."""

    error_task_int_q1 = f"""C'est inexact. Si le 
    {interest_rate} est inférieur au {inflation_rate}, 
    vous ne pouvez qu'en acheter moins."""

    error_task_int_q2 = f"""C'est inexact. Si le 
    {interest_rate} est inférieur au {inflation_rate} et que vous 
    n'avez pas d'{food} en {stock}, vous devez faire des réserves."""

    error_task_int_q3 = f"""C'est inexact. Si le 
    {interest_rate} est supérieur au {inflation_rate}, vous pouvez en
    acheter plus."""

    error_task_int_q4 = f"""C'est inexact. Si le 
    {interest_rate} est supérieur au {inflation_rate} et que vous avez 
    des {food} en {stock}, vous ne devez pas acheter des {food}."""

    error_task_int_q5 = f"""C'est inexact. Si le 
    {interest_rate} est supérieur au {inflation_rate}, vous pouvez en
    acheter plus."""

    error_task_int_q6 = f"""C'est inexact. Si le {interest_rate} 
    est supérieur au {inflation_rate} et que vous avez 0 {unit} 
    d'{food}, vous devez acheter 1 {unit}."""

    error_task_int_q7 = f"""C'est inexact. Si le 
    {interest_rate} est inférieur au {inflation_rate}, vous ne pouvez 
    qu'en acheter moins."""

    error_task_int_q8 = f"""C'est inexact. Si le {interest_rate} est 
    inférieur au {inflation_rate}, que vous estimez que cela doit durer 4 
    mois, et que vous avez 0 {unit} d'{food}, vous devez acheter une 
    quantité égale au nombre que vous estimez de mois dans le future avec un 
    {inflation_rate} supérieur au {interest_rate}."""
