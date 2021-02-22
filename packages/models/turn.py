from datetime import datetime
import match


class Round:
    def __init__(self, name: str):
        self.__name = name
        self.__match_list = []

    def match_list(self, match: match.Match) -> list:
        self.__match_list.append(match.create_match())
        return self.__match_list

    def serialize(self):
        return [{"name": self.__name,
                 "start_datetime": self.start_datetime_round,
                 "end_datetime": self.end_datetime_round,
                 "match_list": self.__match_list}]

    @property
    def name(self) -> str:
        return self.__name

    @property
    def start_datetime_round(self) -> datetime.date:
        self.__start_datetime = datetime.now().isoformat()
        return self.__start_datetime

    @property
    def end_datetime_round(self) -> datetime.date:
        self.__end_datetime = datetime.now().isoformat()
        return self.__end_datetime

