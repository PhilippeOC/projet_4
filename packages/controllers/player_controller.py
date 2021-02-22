from ..models.player_manager import PlayerManager
from ..views.entry_view import EntryView
# from . import menus_controller


class PlayerController:
    def __init__(self):
        self.player_dict = {}
        self.view = EntryView()
        self.players_id = []

    def run(self):
        nb_players = 2
        player_data = {"lastname": "Nom du joueur :",
                       "firstname": "Prénom du joueur :",
                       "datebirth": "Date de naissance : jour-mois-année (ex: 14-02-2000) :",
                       "sex": "Genre : 1.Homme  2.Femme",
                       "ranking": "Classement :"}

        self.view.display_title("Création des huits joueurs", clear_console=False)
        for i in range(nb_players):
            self.view.display_subtitle("Joueurs " + str(i+1))
            for key, data in player_data.items():
                usr_entry = self.view.get_user_entries(data)
                self.player_dict[key] = usr_entry
            # modifs éventuelles des données saisies

            self.player = PlayerManager()
            p = self.player.create_player(self.player_dict)
            self.players_id.append(str(p.identifier))
        
        return self.players_id
