from enum import Enum
#import player


class Match:
    class Score(Enum):
        GAIN = 1
        PERTE = 0
        NUL = 0.5

    def __init__(self, id_player_1, id_player_2, score_player_1, score_player_2):
        self.__id_player_1 = id_player_1
        self.__score_player_1 = score_player_1
        self.__id_player_2 = id_player_2
        self.__score_player_2 = score_player_2

    @property
    def score_player(self) -> float:
        return self.__score_player

    @score_player.setter
    def score_player(self, score_player: float) -> float:
        if score_player not in (self.Score.GAIN.value, self.Score.PERTE.value, self.Score.NUL.value):
            raise self.Error("time_error", "le score doit être : GAIN, PERTE ou NUL")
        self.__score_player = score_player


# main
match_tuple = (['256f7c46-2100-4999-890c-888602998201', 1], ['656i7c46-2100-4999-890c-888602998201', 0])

m1 = Match(*match_tuple)
#print("score:", m1.score_player)
"""#m1.score_player_1 = 0

print("id:", m1.id_player_1)
print("score:", m1.score_player_1)
"""
print("id:", m1.id_player_1)