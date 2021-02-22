from . import utilities


class EntryView:
   
    def display_title(self, title: str, clear_console: bool):
        if clear_console:
            utilities.clear_console()
        utilities.title(title)

    def display_subtitle(self, title: str):
        utilities.subtitle(title)

    """def get_user_entries(self, data: str):
        ok = False
        while not ok:
            user_input = input(data + " >> ")
            rep = input("Souhaitez-vous modifier la saisie , y/n ")
            if rep == "y":
                continue
            else:
                ok = True
            return user_input"""
    
    def get_user_entries(self, data: str):
        user_input = input(data + " >> ")
        return user_input
