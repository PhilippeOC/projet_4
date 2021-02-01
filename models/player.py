import utilities

import datetime
from enum import Enum
from typing import List, NewType, Union
import uuid


class Player:
    class Error(Exception):
        def __init__(self, error_type: str, message: str):
            super().__init__(self, error_type, message)
            self.error_type = error_type
            print("exception:", error_type)

    class Gender(Enum):
        MASCULIN = "M"
        FEMININ = "F"

    def __init__(self, **player_dict: dict):
        for attr_name, attr_value in player_dict.items():
            setattr(self, attr_name, attr_value)

    @property
    def serialize(self) -> dict:
        return {"lastname": self.lastname,
                "firstname": self.firstname,
                "datebirth": self.datebirth,
                "sex": self.sex,
                "ranking": self.ranking,
                "identifier": self.identifier}

    @property
    def identifier(self):
        self.__identifier = uuid.uuid4()
        return self.__identifier

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, last_name: str) -> str:
        if utilities.check_name(last_name):
            raise self.Error("name_error", "Le nom doit contenir au moins deux lettres.")
        self.__lastname = last_name.upper()

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, first_name: str) -> str:
        if utilities.check_name(first_name):
            raise self.Error("first_name_error", "Le prénom doit contenir au moins deux lettres.")
        self.__firstname = first_name.capitalize()

    @property
    def datebirth(self) -> datetime.date:
        return self.__datebirth

    @datebirth.setter
    def datebirth(self, born: List[Union[str, datetime.date]]) -> datetime.date:
        limit_age = 18
        if isinstance(born, str):
            try:
                born = datetime.datetime.strptime(born, '%d-%m-%Y')
            except ValueError:
                raise self.Error("date_error", "{}: vérifier le format de la date.".format(born))
        dt = datetime.date.today()
        age = dt.year - born.year - ((dt.month, dt.day) < (born.month, born.day))
        if age < limit_age:
            raise self.Error("age_error", "Vous devez avoir plus de {} ans pour participer.".format(limit_age))
        self.__datebirth = born

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str) -> str:
        if sex.upper() not in (self.Gender.MASCULIN.value, self.Gender.FEMININ.value):
            raise self.Error("sex_error", "impossible, saisir M ou F.")
        #if sex.upper() not in ('M','F'):
            #raise self.Error("sex_error", "impossible, saisir M ou F.")
        self.__sex = sex.upper()

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, rank: int) -> int:
        self.rank_type = NewType('rank_type', int)
        if not 0 <= self.rank_type(rank) <= 3000:
            raise self.Error("rank_error", "Le classement est un nombre compris entre 0 et 3000.")
        # if not 0 <= rank <= 3000:
            # raise self.Error("rank_error", "Le classement est un nombre compris entre 0 et 3000.")
        self.__ranking = rank


# main
player_dict = {"lastname": "jumbo", "firstname": "babar", "datebirth": "28-01-2000", "sex": "m", "ranking": 100}
player_dict2 = {"lastname": "Starsky", "firstname": "hutch", "datebirth": "01-10-1990", "sex": "f", "ranking": 500}


p1 = Player(**player_dict)
p2 = Player(**player_dict2)

print("id1:", p1.identifier)
print(p1.serialize)
#print(p1.datebirth)

#print("id1:", p1.identifier)
#print("id2:", p2.identifier)
