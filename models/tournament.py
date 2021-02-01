import utilities

import datetime
from enum import Enum
from typing import List, NewType, Union


class Tournament:
    class Error(Exception):
        def __init__(self, error_type: str, message: str):
            super().__init__(self, error_type, message)
            self.error_type = error_type
            print("exception:", error_type)

    class Time(Enum):
        BULLET = "BULLET"
        BLITZ = "BLITZ"
        COUP_RAPIDE = "COUP RAPIDE"

    def __init__(self, **tournament_dict: dict):
        for attr_name, attr_value in tournament_dict.items():
            setattr(self, attr_name, attr_value)

    @property
    def serialize(self) -> dict:
        return {"name": self.name,
                "place": self.place,
                "date": self.date,
                "nb_turns": self.nb_turns,
                "round_list": self.round_list,
                "players_list": self.players_list,
                "time_control": self.time_control,
                "description": self.description
                # identifier ?
                }

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> str:
        if utilities.check_name(name):
            raise self.Error("name_error", "Le nom doit contenir au moins deux lettres.")
        self.__name = name.upper()

    @property
    def place(self) -> str:
        return self.__place

    @place.setter
    def place(self, place: str) -> str:
        if utilities.check_name(place):
            raise self.Error("place_error", "Le nom du lieu doit contenir au moins deux lettres.")
        self.__place = place.capitalize()

    @property
    def date(self) -> datetime.date:
        return self.__date

    @date.setter
    def date(self, day: List[Union[str, datetime.date]]) -> datetime.date:
        if isinstance(day, str):
            try:
                day = datetime.datetime.strptime(day, '%d-%m-%Y')
            except ValueError:
                raise self.Error("date_error", "{}: vérifier le format de la date.".format(day))
        self.__date = day

    @property
    def nb_turns(self) -> int:
        return self.__nb_turns

    @nb_turns.setter
    def nb_turns(self, nb_turns: int) -> int:
        self.nb_turns_type = NewType('nb_turns', int)
        if not self.nb_turns_type(nb_turns) > 0:
            raise self.Error("nb_turns_error", "Le nombre de tours est un nombre entier positif.")
        self.__nb_turns = nb_turns

    @property
    def round_list(self) -> list:
        return self.__round_list

    @round_list.setter
    def round_list(self, round_list: list) -> list:
        self.__round_list = round_list

    @property
    def players_list(self) -> list:
        return self.__players_list

    @players_list.setter
    def players_list(self, players_list: list) -> list:
        self.__players_list = players_list

    @property
    def time_control(self) -> str:
        return self.__time_control

    @time_control.setter
    def time_control(self, time_control: str) -> str:
        if time_control.upper() not in (self.Time.BULLET.value, self.Time.BLITZ.value, self.Time.COUP_RAPIDE.value):
            raise self.Error("time_error", "le contrôle du temps doit être : BULLET, BLITZ ou COUP RAPIDE")
        self.__time_control = time_control.upper()

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> str:
        self.__description = description


# main
tournament_dict = {"name": "tourname",
                   "place": "toulouse",
                   "date": "28-01-2000",
                   "nb_turns": 4,
                   "round_list": ["round 1", "round 2"],
                   "players_list": ["id1", "id2"],
                   "time_control": "Bullet",
                   "description": "commentaire du directeur du tournois"}

t1 = Tournament(**tournament_dict)

print(t1.serialize)
print(t1.place)
