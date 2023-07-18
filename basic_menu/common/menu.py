from basic_menu.common.menuMessage import print_result, print_dictionary_options, print_list_options
from basic_menu.common.prompt import prompt


def menu(options):
    if isinstance(options, dict):
        print_dictionary_options(options)
        selected = prompt(options)
        print_result(options[selected.upper()])

    elif isinstance(options, list):
        print_list_options(options)
        selected = prompt(options)
        print_result(options[int(selected)])
