from enum import Enum
#import player


class Match:
    Score = Enum("Score", [("GAIN", 1), ("PERTE", 0), ("NUL", 0.5)])

    def __init__(self, id_player_1: str, score_player_1: float, id_player_2: str, score_player_2: float):
        self.__id_player_1 = id_player_1
        self.__score_player_1 = score_player_1
        self.__id_player_2 = id_player_2
        self.__score_player_2 = score_player_2
    

    @property
    def score_player_1(self) -> float:
        return self.__score_player_1

    @score_player_1.setter
    def score_player_1(self, score_player_1: float) -> float:
        if score_player_1 not in (self.Score(1).value, self.Score(0).value, self.Score(0.5).value):
            raise self.Error("score_error", "la valeur du score n'est pas correcte")
        self.__score_player_1 = score_player_1

    @property
    def score_player_2(self) -> float:
        return self.__score_player_2

    @score_player_2.setter
    def score_player_2(self, score_player_2: float) -> float:
        if score_player_2 not in (self.Score(1).value, self.Score(0).value, self.Score(0.5).value):
            raise self.Error("score_error", "la valeur du score n'est pas correcte")
        self.__score_player_2 = score_player_2

    def create_match(self) -> tuple:
        #return [(self.__id_player_1, self.__score_player_1), (self.__id_player_2, self.__score_player_2)]
        return ([self.__id_player_1, self.__score_player_1], [self.__id_player_2, self.__score_player_2])
