def print_welcome():
    print("\nWelcome to the menu"
          "\nYou will be presented with some options")


def print_prompt_tutorial():
    print("\n*You may at any point prompt the tutorial by entering /t or redisplay the options with /o*")


def print_tutorial():
    print("\nYou may answer by typing the respective identifier"
          "\n Eg. key (1) for (1.) or key(A/a) for (A/a.)")


def print_selection_menu(input, result):
    print(f"\nYou entered > {input} < which is {result.value}")


def print_result(value):
    print(f"\nYour input selected > {value}")


def print_dictionary_options(options):
    print("")
    for key, value in options.items():
        print(f"Key > {key} < Value > {value} <")


def print_list_options(options):
    print("")
    for index, element in enumerate(options):
        print(f"{index}. {str(element).capitalize()}")
