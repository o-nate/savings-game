# The Savings Game

## Overview
The Savings Game is an intertemporal savings and consumption behavioral economics task designed to measure how inflation impacts individuals' economic decision making. It is designed to integrate into online and laboratory-based behavioral experiments.

The Savings Game operates on the [oTree framework](https://www.otree.org/), using Python, JavaScript, and HTML/CSS. For more information on how to use the `oTree` in python, the [official documentation](https://otree.readthedocs.io/en/latest/index.html).

## Installation
To install and run the Savings Game locally, you will need to ensure to have the requesite dependencies (libraries, packages, etc.), including Python, oTree, and others.

### Using a virtual environment
The simplest way to ensure you correctly install everything is by using a `conda` virtual environment. If you do not have Anaconda installed on your computer, install it first [here](https://www.anaconda.com/download).

Once Anaconda is installed and you have cloned this project repository locally, open a terminal, either in your preferred code-editor (IDE) or directly from your desktop. Navigate to the repository's directory (i.e. folder) in the terminal and execute the following command.
```
conda env create --file environment.yml
```
This will install all the required dependencies with the appropriate version simultaneously. It will also create a 'virtual environment,' which you must activate prior to running the Savings Game.

After the virtual environment creation concludes, activate it by executing the command in the terminal.
```
conda activate savings_game
```
If succesfully activated, you should see `(savings_game)` appear to the left of the folder path in your terminal on the newest line. 

*Congratulations! You are now ready to run the Savings Game.*

## Running the Savings Game
To run the Savings Game locally, open your terminal, either in your preferred code-editor (IDE) or directly from your desktop, and navigate to the repository's directory (i.e. folder) in the terminal. If you created a virtual environment, first activate it using the following command.
```
conda activate savings_game
```

Next, execute:
```
otree devserver
```
If successful, the following message should appear:
```
Open your browser to http://localhost:8000/
To quit the server, press Control+C.
```

Open a web browser and navigate to the address `http://localhost:8000/`. The screen below should appear in the window.

![image](https://github.com/le-nate/the_savings_game/assets/99023298/e927dcb3-d6be-4091-bd96-fe6dd7213cb2)

## Testing
As describe further in the following sections, the Savings Game requires certain variables (e.g. the inflation sequence) be defined in order to run. When in production (i.e. when an experiment is actively being conducted) these variables will be defined outside of the Savings Game itself. So, when testing, we must define them manually. These variables get assigned by a module `filler`, which executes prior to the Savings Game task when you click on `The Savings Game` or `The Savings Game (Standalone)`. We explain how to adjust these variables in the later sections. For now, you just need to know that this means that when testing, a page will appear beforehand saying "This is a blank page required during testing to set certain participant_field values prior to beginning." This message is not intended to appear during an experiment.

## Apps
### The Savings Game
`savings_game`
The Savings Game code is separated into an `__init__.py`, which acts at the "backend" of the program. The "frontend", which provides the user interface and is what the subjects interact with is stored in the HTML files within `savings_game`. The inflation sequences are defined in `animal_spirits.csv` and the products available in `catalog.csv`. To define the inflation sequence, in the `filler` app, set: 
```
player.participant.inflation = [1012, 430]
```

### Filler (For testing and debugging purposes only)
The `filler` app is necessary for testing the apps as standalones. It adds values certain `participant_fields`.

### Instructions
The `instructions` app acts as a standalone to view the instructions for the Savings Game. Make sure to define the `player.participant.instructions` in `filler`.

### Interventions
There are three apps for the different interventions used in the first (`intervention`) and second (`intervention_1` and `intervention_2`) experiment. Make sure to define in `filler`:
```
player.participant.intervention = "treatment"
```

In `intervention_1` and `intervention_2`, if you would like to test new dynamic responses to different combinations of errors, adjust:
```
errors_dict = {"early": 1, "late": 1, "excess": 0}
```

## Settings
Setting can be defined in two places, either in the experiment-wide `SESSION_CONFIG_DEFAULTS` dictionary in `settings.py` or in the `C` class of the `__init__.py` file for a specific app. Settings defined in `SESSION_CONFIG_DEFAULTS` apply across all apps in the experiment. Settings defined in the `C` class of an app are app-specific.

## Multi-language
The program offers multi-language support, currently in English and French. To define the language of the experiment, simply change the value of `LANGUAGE_CODE` in `settings.py`, using the ISO-639 code (`en` for English, `fr` for French).

### Adjusting text
The multi-language functionality means that text can be defined in one of two ways throughout the program. Terms and phrases that are repeated throughout the experiment are defined in the `_static/lexicon_en.py` and `_static/lexicon_fr.py` files.

Each file contains a class `Lexicon` with the same attributes (i.e. variables), one for each term or phase. These attributes are then referenced where necessary in the `__init__.py` and HTML files.

The text for questions, defined in `Player`, are set via the `Lexicon` class. To change the text of the question, we have to change the text in the corresponding attributes in the two `_static/lexicon_en.py` and `_static/lexicon_fr.py` files.

For examle, if we want to change the text of the first question in the `instructions.py`, we update the text for `Lexicon.q1` in `_static/lexicon_en.py` and `_static/lexicon_fr.py` (assuming we will use both languages). If we want to change the text displayed on the button to finalize a purchase, we update the text for `Lexicon.finalize_purchase` in both files, and the text will be update across the complete experiment. 

In the HTML files, terms and phrase from `Lexicon` are inserted via the Django dependency. To add a term or phrase from `Lexicon` into text in the HTML, use the `{{}}` with the attribute.

For example:
```
<p>
    Here is an example using the term for {{ Lexicon.food }}
</p>
```

### Adding a new language
To add a new language, copy one of the lexicon files, adding the language to the file name. Then, replace the terms in the attributes. 
After, in each `__init__.py` file, add the language to the following:
```
if LANGUAGE_CODE == "fr":
    from _static.lexicon_fr import Lexicon
elif LANGUAGE_C0DE == "new_language_code"
    from _static.lexicon_new_language_code import Lexicon
else:
    from _static.lexicon_en import Lexicon

# This is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if fr }} Oui {{ else }} Yes {{ endif }}
which_language = {"en": False, "fr": False, "new_language_code": False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True
```