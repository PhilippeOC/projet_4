
from .tournament_controller import TournamentController
from .quit_controller import QuitController

from ..utils.menus import Menu
from ..views.menu_view import MenuView


class HomeMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.title = "Accueil"
        self.menu.add("auto", "Créer un nouveau tournoi", TournamentController())
        self.menu.add("auto", "Consulter les rapports", ReportsMenuController())
        self.menu.add("auto", "Quitter le programme", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice


class ReportsMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.title = "Rapports"
        self.menu.add("auto", "Liste des acteurs par ordre alphabétique", None)
        self.menu.add("auto", "Liste des acteurs par classement", None)
        self.menu.add("auto", "Liste des joueurs d'un tournoi par ordre alphabetique", None)
        self.menu.add("auto", "Liste des joueurs d'un tournoi par classement",  None)
        self.menu.add("auto", "Liste de tous les tournois", None)
        self.menu.add("auto", "Liste de tous les tours d'un tournoi", None)
        self.menu.add("auto", "Liste de tous les matchs d'un tournoi", None)
        self.menu.add("auto", "Menu précédent", HomeMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice
