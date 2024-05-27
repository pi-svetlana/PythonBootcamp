from enum import Enum


class Choice(Enum):
    COOPERATE = 0
    CHEAT = 1


class Result(Enum):
    BOTH_COOPERATE = 0
    ONLY_I_COOPERATE = 1
    ONLY_I_CHEAT = 2
    BOTH_CHEAT = 3

    @staticmethod
    def result_of_match(p1_choice: Choice, p2_choice: Choice):
        if p1_choice == Choice.COOPERATE and p2_choice == Choice.COOPERATE:
            return Result.BOTH_COOPERATE
        elif p1_choice == Choice.COOPERATE and p2_choice == Choice.CHEAT:
            return Result.ONLY_I_COOPERATE
        elif p1_choice == Choice.CHEAT and p2_choice == Choice.COOPERATE:
            return Result.ONLY_I_CHEAT
        elif p1_choice == Choice.CHEAT and p2_choice == Choice.CHEAT:
            return Result.BOTH_CHEAT


class Player:
    def __init__(self):
        self.type: PlayerType = PlayerType.DEFAULT

    @staticmethod
    def create_player(player_type):
        if player_type == PlayerType.CHEATER:
            return Cheater()
        elif player_type == PlayerType.COOPERATOR:
            return Cooperator()
        elif player_type == PlayerType.COPYCAT:
            return Copycat()
        elif player_type == PlayerType.GRUDGER:
            return Grudger()
        elif player_type == PlayerType.DETECTIVE:
            return Detective()
        elif player_type == PlayerType.MYPLAYER:
            return MyPlayer()
        else:
            return Player()

    @staticmethod
    def count_score(res: Result):
        change_score = 0
        if res == Result.BOTH_COOPERATE:
            change_score = 2
        if res == Result.ONLY_I_CHEAT:
            change_score = 3
        if res == Result.ONLY_I_COOPERATE:
            change_score = -1
        return change_score

    def move(self):
        pass

    def reset(self):
        pass


class PlayerType(Enum):
    DEFAULT = 0
    CHEATER = 1
    COOPERATOR = 2
    COPYCAT = 3
    GRUDGER = 4
    DETECTIVE = 5
    MYPLAYER = 6

    @staticmethod
    def extract_name_from_id(num):
        return PlayerType(num % len(PlayerType))


class Cheater(Player):
    def __init__(self):
        super().__init__()
        self.type: PlayerType = PlayerType.CHEATER

    def move(self):
        return Choice.CHEAT


class Cooperator(Player):
    def __init__(self):
        super().__init__()
        self.type: PlayerType = PlayerType.COOPERATOR

    def move(self):
        return Choice.COOPERATE


class Copycat(Player):
    def __init__(self):
        super().__init__()
        self.type: PlayerType = PlayerType.COPYCAT
        self.step = Choice.COOPERATE

    def count_score(self, res: Result):
        if res == Result.BOTH_COOPERATE or res == Result.ONLY_I_CHEAT:
            self.step = Choice.COOPERATE
        else:
            self.step = Choice.CHEAT
        return super().count_score(res)

    def move(self):
        return self.step

    def reset(self):
        self.step = Choice.COOPERATE


class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.type: PlayerType = PlayerType.GRUDGER
        self.flag_cheat = False
        self.step = Choice.COOPERATE

    def count_score(self, res: Result):
        if res == Result.ONLY_I_COOPERATE:
            self.flag_cheat = True
        if self.flag_cheat:
            self.step = Choice.CHEAT
        return super().count_score(res)

    def move(self):
        return self.step

    def reset(self):
        self.step = Choice.COOPERATE
        self.flag_cheat = False


class Detective(Player):
    def __init__(self):
        super().__init__()
        self.type: PlayerType = PlayerType.DETECTIVE
        self.flag_cheat = False
        self.step = Choice.COOPERATE
        self.steps: list = [Choice.CHEAT, Choice.COOPERATE, Choice.COOPERATE]

    def count_score(self, res: Result):
        if len(self.steps) > 0:
            self.step = self.steps.pop(0)
            if res == Result.ONLY_I_COOPERATE or res == Result.BOTH_CHEAT:
                self.flag_cheat = True
        else:
            if self.flag_cheat:
                self.step = Choice.CHEAT
            else:
                if res == Result.BOTH_COOPERATE or res == Result.ONLY_I_CHEAT:
                    self.step = Choice.COOPERATE
                else:
                    self.step = Choice.CHEAT
        return super().count_score(res)

    def move(self):
        return self.step

    def reset(self):
        self.step = Choice.COOPERATE
        self.flag_cheat = False


class MyPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type: PlayerType = PlayerType.MYPLAYER
        self.step = Choice.COOPERATE
        self.steps: list = [Choice.COOPERATE, Choice.COOPERATE]

    def count_score(self, res: Result):
        if len(self.steps) > 0:
            self.step = self.steps.pop(0)
        else:
            if res == Result.BOTH_COOPERATE or res == Result.ONLY_I_CHEAT:
                self.step = Choice.COOPERATE
            else:
                self.step = Choice.CHEAT
        return super().count_score(res)

    def move(self):
        return self.step

    def reset(self):
        self.step = Choice.COOPERATE
