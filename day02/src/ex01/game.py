from collections import Counter

from players import Player, PlayerType, Result


class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        player1.reset()
        player2.reset()
        for k in range(self.matches):
            step_1 = player1.move()
            step_2 = player2.move()
            self.registry[player1.type.value] += player1.count_score(Result.result_of_match(step_1, step_2))
            self.registry[player2.type.value] += player2.count_score(Result.result_of_match(step_2, step_1))

    def top3(self):
        print('=== TOP-3 ===')
        for player in self.registry.most_common(len(self.registry)):
            player_type = PlayerType.extract_name_from_id(player[0])
            print(f'{player_type.name.title()} - {player[1]}')


if __name__ == "__main__":
    first_game = Game()
    player = Player()

    print('= First game =')
    for i in range(PlayerType.CHEATER.value, PlayerType.DETECTIVE.value):
        for j in range(i + 1, PlayerType.DETECTIVE.value + 1):
            player_1 = player.create_player(PlayerType(i))
            player_2 = player.create_player(PlayerType(j))
            first_game.play(player_1, player_2)
    first_game.top3()
    print()

    second_game = Game()
    print('= Second game =')
    for i in range(PlayerType.CHEATER.value, PlayerType.MYPLAYER.value):
        for j in range(i + 1, PlayerType.MYPLAYER.value + 1):
            player_1 = player.create_player(PlayerType(i))
            player_2 = player.create_player(PlayerType(j))
            second_game.play(player_1, player_2)
    second_game.top3()
