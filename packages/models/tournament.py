from . import utilities

import datetime
from enum import Enum
from typing import Union


class Tournament:
    class Error(Exception):
        def __init__(self, error_type: str, message: str):
            super().__init__(self, error_type, message)
            self.error_type = error_type
            print("exception:", error_type)

    Time = Enum('Time', ['BULLET', 'BLITZ', 'COUP RAPIDE'])

    def __init__(self, **tournament_dict: dict):
        """for attr_name, attr_value in tournament_dict.items():
            setattr(self, attr_name, attr_value)"""
        for attr_name in ("name", "place", "date", "nb_turns", "round_list", "players_id_list", "time_control", "description"):
            setattr(self, attr_name, tournament_dict[attr_name] if attr_name in tournament_dict else None)
        self.__identifier = self.name + "-" + self.place + "-" + self.date.isoformat()

    @property
    def serialize(self) -> dict:
        return {"name": self.name,
                "place": self.place,
                "date": self.date.isoformat(),
                "nb_turns": self.nb_turns,
                "round_list": self.round_list,
                "players_id_list": self.players_id_list,
                "time_control": self.time_control,
                "description": self.description
                }

    @property
    def identifier(self) -> str:
        return self.__identifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if not utilities.check_name(name):
            raise self.Error("name_error", "Le nom doit contenir au moins deux lettres.")
        self.__name = name.upper()

    @property
    def place(self) -> str:
        return self.__place

    @place.setter
    def place(self, place: str):
        if not utilities.check_name(place):
            raise self.Error("place_error", "Le nom du lieu doit contenir au moins deux lettres.")
        self.__place = place.capitalize()

    @property
    def date(self) -> datetime.date:
        return self.__date

    @date.setter
    def date(self, day: Union[str, datetime.date]):
        if isinstance(day, str):
            try:
                day = datetime.datetime.strptime(day, '%d-%m-%Y')
            except ValueError:
                raise self.Error("date_error", f"{day}: vérifier le format de la date.")
        self.__date = day

    @property
    def nb_turns(self) -> int:
        return self.__nb_turns

    @nb_turns.setter
    def nb_turns(self, nb_turns: Union[str, int]):
        if isinstance(nb_turns, str):
            nb_turns = int(nb_turns)
        if not nb_turns > 0:
            raise self.Error("nb_turns_error", "Le nombre de tours est un nombre entier positif.")
        self.__nb_turns = nb_turns

    @property
    def round_list(self) -> list:
        return self.__round_list

    @round_list.setter
    def round_list(self, round_list: list):
        self.__round_list = round_list

    @property
    def players_id_list(self) -> list:
        return self.__players_id_list

    @players_id_list.setter
    def players_id_list(self, players_id: list):
        self.__players_id_list = players_id

    @property
    def time_control(self) -> str:
        return self.__time_control

    @time_control.setter
    def time_control(self, time_control: str):
        time_control = int(time_control)
        if time_control not in [item.value for item in self.Time]:
            raise self.Error("time_error", "le contrôle du temps doit être : BULLET, BLITZ ou COUP RAPIDE")
        for item in self.Time:
            if time_control == item.value:
                self.__time_control = item.name
                break

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description
