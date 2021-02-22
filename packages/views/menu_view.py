from . import utilities


class MenuView:
    def __init__(self, menu):
        self.menu = menu
        self.items = self.menu.items_menu()

    def __display_menu(self):
        utilities.clear_console()
        utilities.title(self.menu.title)
        for key, menu_content in self.items.items():
            print(f"{key}: {menu_content.item_menu}")

    def get_user_choice(self):
        while True:
            self.__display_menu()
            choice = input("Votre choix: >> ")
            if self.menu.valid_key(choice):
                return self.items[str(choice)].action_menu
