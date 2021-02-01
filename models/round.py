import datetime


class Round:
    def __init__(self, **round_dict: dict):
        for attr_name, attr_value in round_dict.items():
            setattr(self, attr_name, attr_value)

    @property
    def datetime_round(self) -> datetime.date:
        return self.__datetime_round.today()

    @datetime_round.setter
    def datetime_round(self, datetime_round) -> datetime.date:
        self.__datetime_round = datetime_round


# main
round_dict = {"name": "Round 1",
              "start_datetime": "28-01-2000 20:15:30",
              "end_datetime": "28-01-2000 23:01:05",
              "match_list": [("id player1", "score"), ("id player2", "score")]
              }

r1 = Round(**round_dict)
