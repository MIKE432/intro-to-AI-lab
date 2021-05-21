from abstracts.Game import Game
from abstracts.Player import Player
from implementations.BotPlayer import BotPlayer
from implementations.MancalaDecisionTree import MancalaDecisionNode, apply_decision_tree_to_root, add_one_level
from implementations.MancalaTools import get_opposite_index, end_condition_mancala, validate_indexes, validate_number, \
    move_from_to, turn


class Mancala(Game):
    def __init__(self, player1: Player, player2: Player):
        super().__init__(player1, player2)
        self.board = []
        self.__init_board()

    def pick_first_player(self):
        self.current_player = self.players[0]

    def __init_board(self):
        for i in range(0, 14):
            if i in [6, 13]:
                self.board.append(0)
            else:
                self.board.append(4)

    def get_player_choices(self):
        start, end = (0, 6) if self.current_player == self.players[0] else (7, 13)
        return list(filter(lambda _x: self.board[_x] != 0, list(range(start, end))))

    def end_condition(self):
        return end_condition_mancala(self.board)

    def turn_procedure(self):
        turn(self.board, self.current_player, True)

    def __str__(self):
        s = "      " + str(list(reversed(self.board[7:13]))) + "\n" + str(
            self.board[13]) + "                         " + str(
            self.board[6]) + "\n" + "      " + str(self.board[:6]) + "\n"
        return s

    def sum_points(self):
        player1 = sum(self.board[:7])
        player2 = sum(self.board[7:])

        return player1, player2


def AIvsAI(game, disable_print=False):
    first_turn = True
    while not game.end_condition():
        turn(game.board, game.current_player,  first_turn)
        first_turn = False
        game.switch_players()
        if not disable_print:
            print(game)
    print(game.sum_points())
