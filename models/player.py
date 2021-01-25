import datetime


class PlayerExcept(Exception):
    def __init__(self, error_type, message):
        Exception.__init__(self, error_type, message)
        self.error_type = error_type
        print("exception:", error_type)


class Player:
    def __init__(self, **player_dict):
        for attr_name, attr_value in player_dict.items():
            setattr(self, attr_name, attr_value)

    def serialize(self, serialized_players):
        p_dict = {"lastname": self.__lastname, "firstname": self.__firstname, "datebirth": self.__datebirth, "sex": self.__sex, "ranking": self.__ranking}
        serialized_players.append(p_dict)
        return serialized_players

    def alphabetical_order(self, serialized_players):
        pass
        return serialized_players

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, last_name):
        if len(last_name) < 2:
            raise PlayerExcept("name_error", "Le nom doit contenir au moins deux caractères")
        self.__lastname = last_name.upper()

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, first_name):
        if len(first_name) < 2:
            raise PlayerExcept("first_name_error", "Le prénom doit contenir au moins deux caractères")
        self.__firstname = first_name.capitalize()

    @property
    def datebirth(self):
        return self.__datebirth

    @datebirth.setter
    def datebirth(self, born):
        limit_age = 18
        try:
            db = datetime.datetime.strptime(born, '%d-%m-%Y')
        except ValueError:
            raise PlayerExcept("date_error", "{}: vérifier le format de la date".format(born))
        else:
            dt = datetime.date.today()
            age = dt.year - db.year - ((dt.month, dt.day) < (db.month, db.day))
            if age < limit_age:
                raise PlayerExcept("age_error", "Vous devez avoir plus de {} ans pour participer".format(limit_age))
            print("age:", str(age) + " ans")
        self.__datebirth = born

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if sex.upper() != 'M':
            if sex.upper() != 'F':
                raise PlayerExcept("sex_error", "impossible, saisir M ou F")
        self.__sex = sex.upper()

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, rank):
        # validations
        self.__ranking = rank


# main
serialized_players = []
player_dict = {"lastname": "jumbo", "firstname": "babar", "datebirth": "18-01-1958", "sex": "f", "ranking": 100}
player_dict2 = {"lastname": "Starsky", "firstname": "hutch", "datebirth": "01-10-1990", "sex": "m", "ranking": 1500}


p1 = Player(**player_dict)
p2 = Player(**player_dict2)

print(p1.serialize(serialized_players))
print(p2.serialize(serialized_players))

print(player_dict)
print(player_dict2)

print("date de naissance 1:", p1.datebirth)
print("prénom 1:", p1.firstname)

print("date de naissance 2:", p2.datebirth)
print("prénom 2:", p2.firstname)
