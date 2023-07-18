from basic_menu.common.menuMessage import print_selection_menu, print_prompt_tutorial
from basic_menu.common.results import Results
from basic_menu.common.menuInputEquater import main_input_equator

valid = Results.NULL
fails = 0
res = None
value = None


def prompt(options):
    global fails
    global res
    global value
    global valid

    while valid != Results.VALID:
        fails = handle_fail()
        value = input("\n> ").upper()
        res = main_input_equator(options, value.upper())
        valid = handle_output()

    return value.upper()


def handle_output():
    global res
    global fails
    print_selection_menu(value, res)
    if res != Results.COMMAND or res != Results.VALID:
        fails += 1
    return res


def handle_fail():
    global fails
    if fails % 3 == 0 and fails != 0:
        print_prompt_tutorial()
        return 0
    return fails
