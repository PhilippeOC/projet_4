from ..models.tournament import Tournament
from ..views.entry_view import EntryView
from . import menus_controller
from .player_controller import PlayerController


class TournamentController:
    def __init__(self):
        self.tournament_dict = {}
        self.view = EntryView()
        self.player_controller = PlayerController()

    def run(self):
        tournament_data = {"name": "Nom du tournoi :",
                           "place": "Lieu du tournoi :",
                           "date": "Date du tournoi: jour-mois-année (ex: 14-02-2021) :",
                           "nb_turns": "Nombre de tours (4 par défaut):",
                           "time_control": "Contrôle du temps : 1.Bullet  2.Blitz  3.Coup rapide",
                           "description": "Commentaire du directeur du tournoi :"}

        self.view.display_title("Création d'un tournoi", clear_console=True)
        for key, data in tournament_data.items():
            usr_entry = self.view.get_user_entries(data)
            if key == "nb_turns" and usr_entry == '':
                usr_entry = '4'     # valeur par défaut du nombre de tours
            self.tournament_dict[key] = usr_entry

        # modifs éventuelles des données saisies
        self.tournament_dict["players_id_list"] = self.player_controller.run()
        self.tournament = Tournament(**self.tournament_dict)
        print(self.tournament.serialize)    # print de débug
        
        #return menus_controller.HomeMenuController()
