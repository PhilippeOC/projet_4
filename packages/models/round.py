
from datetime import datetime


class Round:
    def __init__(self, **round_dict: dict):
        for attr_name, attr_value in round_dict.items():
            setattr(self, attr_name, attr_value)


    @property
    def start_datetime_round(self):
        self.__start_datetime = datetime.now().isoformat()
        return self.__start_datetime
    
    @property
    def end_datetime_round(self):
        self.__end_datetime = datetime.now().isoformat()
        return self.__end_datetime


# main
round_dict = {"name": "Round 1",
              "start_datetime": "28-01-2000 20:15:30",
              "end_datetime": "28-01-2000 23:01:05",
              "match_list": [("id player1", "score_1"), ("id player2", "score_2")]
              }

r1 = Round(**round_dict)
print(round_dict)
print('date debut:', r1.start_datetime_round)
print('date fin:', r1.end_datetime_round)
