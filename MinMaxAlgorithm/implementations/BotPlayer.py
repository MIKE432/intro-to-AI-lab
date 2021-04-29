from copy import deepcopy
from random import randint

from Tools import get_other_player
from abstracts.Player import Player
from implementations.MancalaDecisionTree import MancalaDecisionNode, apply_decision_tree_to_root, \
    prepare_tree_for_min_max
from implementations.MancalaTools import end_condition_mancala, evaluate_function, move_chosen_pieces
from implementations.MinmaxTools import min_max, min_max2


class BotPlayer(Player):
    def __init__(self, number, difficulty):
        super().__init__(number)
        self.difficulty = difficulty

    def move(self, choices, board, root, random_move=False):
        if random_move:
            return choices[randint(0, len(choices) - 1)]

        max = -1000
        _choice = 0
        for choice in choices:
            b = deepcopy(board)
            another_turn = move_chosen_pieces(b, self.tag, choice)
            value = min_max2(b, get_other_player(
                self.tag) if not another_turn else self.tag - 1, self.difficulty, self.tag, end_condition_mancala,
                             evaluate_function, -100000000, 100000000)

            if value > max:
                max = value
                _choice = choice
        print(f"Bot {self.tag} picked {_choice}")
        return _choice
