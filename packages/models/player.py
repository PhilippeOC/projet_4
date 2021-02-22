from . import utilities

import datetime
from enum import Enum
from typing import Union
import uuid


class Player:
    class Error(Exception):
        def __init__(self, error_type: str, message: str):
            super().__init__(self, error_type, message)
            print("exception:", error_type)

    #Gender = Enum("Gender", [("MALE", "M"), ("FEMALE", "F")])
    Gender = Enum("Gender", "Homme Femme")

    def __init__(self, **player_dict: dict):
        for attr_name in ("identifier", "lastname", "firstname", "sex", "datebirth", "ranking"):
            setattr(self, attr_name, player_dict[attr_name] if attr_name in player_dict else None)

    def serialize(self) -> dict:
        return {"lastname": self.lastname,
                "firstname": self.firstname,
                "datebirth": self.datebirth.isoformat(),
                "sex": self.sex,
                "ranking": self.ranking,
                "identifier": str(self.identifier)
                }

    @property
    def identifier(self) -> uuid.UUID:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: Union[uuid.UUID, str]):
        if value is None:
            self.__identifier = uuid.uuid4()
        elif isinstance(value, str):
            try:
                value = uuid.uuid4(value)
            except:
                pass
                #raise self.Error("value_error", "L'attribution d'un identifiant a échoué")
            self.__identifier = value
        elif isinstance(value, uuid.UUID):
            if value.version != 4:
                raise self.Error("version_error", "La version du numéro de l'identifiant n'est pas correcte")
            self.__identifier = value

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, last_name: str):
        if not utilities.check_name(last_name):
            raise self.Error("name_error", "Le nom doit contenir au moins deux lettres.")
        self.__lastname = last_name.upper()

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, first_name: str):
        if not utilities.check_name(first_name):
            raise self.Error("first_name_error", "Le prénom doit contenir au moins deux lettres.")
        self.__firstname = first_name.capitalize()

    @property
    def datebirth(self) -> datetime.date:
        return self.__datebirth

    @datebirth.setter
    def datebirth(self, born: Union[str, datetime.date]):
        age_min = 18
        age_max = 100
        if isinstance(born, str):
            try:
                born = datetime.datetime.strptime(born, '%d-%m-%Y')
            except ValueError:
                raise self.Error("date_error", f"{born}: vérifier le format de la date.")
        dt = datetime.date.today()
        age = dt.year - born.year - ((dt.month, dt.day) < (born.month, born.day))
        if not age_min < age < age_max:
            raise self.Error("age_error", f"Vous devez avoir entre {age_min} et {age_max} ans pour participer.")
        self.__datebirth = born

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        sex = int(sex)
        if sex not in [item.value for item in self.Gender]:
            raise self.Error("gender_error", "impossible, saisir Homme ou Femme.")
        for item in self.Gender:
            if sex == item.value:
                self.__sex = item.name
                break

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, rank: str):
        rank_min = 0
        rank_max = 3000
        rank = int(rank)
        if not rank_min <= rank <= rank_max:
            raise self.Error("rank_error", f"Le classement est un nombre compris entre {rank_min} et {rank_max}.")
        self.__ranking = rank

