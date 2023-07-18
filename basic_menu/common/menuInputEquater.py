from basic_menu.common.menuMessage import print_tutorial, print_dictionary_options, print_list_options
from basic_menu.common.results import Results


def main_input_equator(options, input):
    # print(type(options), type(input))
    if handle_commands(options, input):
        return Results.COMMAND
    if isinstance(options, dict):
        return menu_input_equator_dictionary(options, input)
    elif isinstance(options, list):
        return menu_input_equator_list(options, input)


def menu_input_equator_dictionary(options, input):
    if input in options:
        return Results.VALID
    else:
        return Results.ERROR


def menu_input_equator_list(options, input):
    try:
        input_int = int(input)
        if not input.isdigit():
            return Results.INVALID

        if input_int > len(options) or input_int < 0:
            return Results.OUT_OF_RANGE

        if options[input_int] is not None:
            return Results.VALID

        return Results.UNDETERMINED
    except:
        return Results.ERROR


def handle_commands(options, input):
    if input.upper() == "/t".upper():
        print_tutorial()
        return True
    elif input.upper() == "/o".upper():
        if isinstance(options, dict):
            print_dictionary_options(options)
        elif isinstance(options, list):
            print_list_options(options)
        return True
    else:
        return False
