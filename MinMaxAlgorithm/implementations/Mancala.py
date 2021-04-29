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
        self.decision_tree = self.__init_decision_tree()

    def pick_first_player(self):
        self.current_player = self.players[0]

    def __init_board(self):
        for i in range(0, 14):
            if i in [6, 13]:
                self.board.append(0)
            else:
                self.board.append(4)

    def __init_decision_tree(self):
        depth = 0
        if isinstance(self.players[0], BotPlayer) and isinstance(self.players[1], BotPlayer):
            depth = max(self.players[0].difficulty, self.players[1].difficulty)

        node = MancalaDecisionNode(self.board, self.current_player.tag, -1)
        if depth > 0:
            apply_decision_tree_to_root(self.board, node, depth + 1)
            return node

    def get_player_choices(self):
        start, end = (0, 6) if self.current_player == self.players[0] else (7, 13)
        return list(filter(lambda _x: self.board[_x] != 0, list(range(start, end))))

    def end_condition(self):
        return end_condition_mancala(self.board)

    def update_after_turn(self, choice):
        if self.decision_tree:
            for child in self.decision_tree.children:
                if child.after_picking == choice:
                    self.decision_tree = child

        if self.decision_tree:
            add_one_level(self.decision_tree)

    def root(self):
        return self.decision_tree

    def turn_procedure(self):
        turn(self.board, self.current_player, self.root, False, self.update_after_turn)

    def __str__(self):
        s = "      " + str(list(reversed(self.board[7:13]))) + "\n" + str(
            self.board[13]) + "                         " + str(
            self.board[6]) + "\n" + "      " + str(self.board[:6]) + "\n"
        return s

    def sum_points(self):
        player1 = sum(self.board[:7])
        player2 = sum(self.board[7:])

        return player1, player2


def AIvsAI(game):
    first_turn = True
    while not game.end_condition():
        turn(game.board, game.current_player, game.decision_tree,  first_turn, game.update_after_turn)
        first_turn = False
        game.switch_players()
        print(game)
    print(game.sum_points())
