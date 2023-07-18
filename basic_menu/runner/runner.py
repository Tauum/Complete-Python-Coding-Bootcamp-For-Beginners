from basic_menu.common.loadData import load_dictionary, load_list
from basic_menu.common.menu import menu
from basic_menu.common.menuMessage import print_welcome, print_prompt_tutorial

if __name__ == '__main__':
    print_welcome()
    print_prompt_tutorial()
    menu(
        load_dictionary()
        # load_list()
    )
