import player_manager
from .tournament import Tournament
import player

PLAYERS = [{"identifier": '6861d44a-e844-4d9c-852d-f70cde7efbc7', "lastname": "jumbo", "firstname": "BABAR", "datebirth": "28-01-2000", "sex": "m", "ranking": 100},
           {"identifier": '19545c64-d301-4150-b1e8-22f944bc07d6', "lastname": "Starsky", "firstname": "hutch", "datebirth": "01-10-1990", "sex": "m", "ranking": 500},
           {"identifier": '60a43ced-49f8-4d04-8d50-f8ce4231b216', "lastname": "jackson", "firstname": "michael", "datebirth": "25-08-1965", "sex": "m", "ranking": 1000},
           {"identifier": 'aaed9696-2c0c-4eb0-8940-c281a461f383', "lastname": "Poe", "firstname": "edgar", "datebirth": "01-10-1930", "sex": "m", "ranking": 2000},
           {"identifier": '6025f0b0-5a1e-402c-8662-102d47949243', "lastname": "macron", "firstname": "emmanuel", "datebirth": "21-12-1977", "sex": "m", "ranking": 0},
           {"identifier": '05a155db-573b-4554-9c76-abc4112f5440', "lastname": "macron", "firstname": "brigitte", "datebirth": "13-04-1953", "sex": "f", "ranking": 2},
           {"identifier": '8037eff0-e137-4117-8a64-ca642a1923c9', "lastname": "bardot", "firstname": "brigitte", "datebirth": "28-09-1934", "sex": "f", "ranking": 2500},
           {"identifier": '6b19ac83-a2ff-413f-b8a0-2dd927b77da4', "lastname": "sharapova", "firstname": "maria", "datebirth": "19-04-1987", "sex": "f", "ranking": 3000}
           ]

tournament_dict = {"name": "tourname", "place": "toulouse", "date": "28-01-2000",
                   "nb_turns": 4,
                   "round_list": [
                                  {"name": "Round 1",
                                   "start_datetime": "2000-28-01T14:05:30",
                                   "end_datetime": "2000-28-01T17:15:50",
                                   "match_list": [
                                                  (['6861d44a-e844-4d9c-852d-f70cde7efbc7', 0.5]), (['19545c64-d301-4150-b1e8-22f944bc07d6', 0.5]),
                                                  (['60a43ced-49f8-4d04-8d50-f8ce4231b216', 1]), (['aaed9696-2c0c-4eb0-8940-c281a461f383', 0]),
                                                  (['6025f0b0-5a1e-402c-8662-102d47949243', 0]), (['05a155db-573b-4554-9c76-abc4112f5440', 1]),
                                                  (['8037eff0-e137-4117-8a64-ca642a1923c9', 0.5]), (['6b19ac83-a2ff-413f-b8a0-2dd927b77da4', 0.5]),
                                                  ]
                                   },
                                  {"name": "Round 2",
                                   "start_datetime": "2004-28-01T10:35:50",
                                   "end_datetime": "2004-28-01T19:13:15",
                                   "match_list": [
                                                  (['6861d44a-e844-4d9c-852d-f70cde7efbc7', 0.5]), (['19545c64-d301-4150-b1e8-22f944bc07d6', 0.5]),
                                                  (['60a43ced-49f8-4d04-8d50-f8ce4231b216', 1]), (['aaed9696-2c0c-4eb0-8940-c281a461f383', 0]),
                                                  (['6025f0b0-5a1e-402c-8662-102d47949243', 0]), (['05a155db-573b-4554-9c76-abc4112f5440', 1]),
                                                  (['8037eff0-e137-4117-8a64-ca642a1923c9', 0.5]), (['6b19ac83-a2ff-413f-b8a0-2dd927b77da4', 0.5]),
                                                  ]
                                   }],
                   "players_id_list": ['6861d44a-e844-4d9c-852d-f70cde7efbc7',
                                       '19545c64-d301-4150-b1e8-22f944bc07d6',
                                       '60a43ced-49f8-4d04-8d50-f8ce4231b216',
                                       'aaed9696-2c0c-4eb0-8940-c281a461f383',
                                       '6025f0b0-5a1e-402c-8662-102d47949243',
                                       '05a155db-573b-4554-9c76-abc4112f5440',
                                       '8037eff0-e137-4117-8a64-ca642a1923c9',
                                       '6b19ac83-a2ff-413f-b8a0-2dd927b77da4'],
                   "time_control": "Bullet",
                   "description": "commentaire du directeur du tournois"}


pm = player_manager.PlayerManager()
for data in PLAYERS:
    p = pm.create_player(data)

"""dico = pm.find_all()
for k, attr in dico.items():
    print("id du joueur:", k, "attributs:", attr.lastname, attr.firstname)
"""

t1 = Tournament(**tournament_dict)
"""
print("name:", t1.name, "lieu:", t1.place, "date:", t1.date)
print("rounds:", t1.round_list)
print("id players:", t1.players_id_list)
"""
print(t1.serialize)
print(t1.identifier)








































