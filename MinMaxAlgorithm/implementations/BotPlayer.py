from random import randint

from abstracts.Player import Player
from implementations.MancalaDecisionTree import MancalaDecisionNode, apply_decision_tree_to_root
from implementations.MancalaTools import end_condition_mancala, evaluate_function
from implementations.MinmaxTools import min_max


class BotPlayer(Player):
    def __init__(self, number, difficulty):
        super().__init__(number)
        self.difficulty = difficulty

    def move(self, choices, board, random_move=False):
        if random_move:
            return choices[randint(0, len(choices) - 1)]
        root = MancalaDecisionNode(board, self.tag, -1)
        apply_decision_tree_to_root(board, root, self.difficulty + 1)
        min_max(root, self.difficulty, self.tag, end_condition_mancala, evaluate_function, -100000000, 100000000)
        choice = list(sorted(root.children, key=lambda _x: (-1) * _x.value))[0].after_picking
        print(f"Bot {self.tag} picked {choice}")
        return choice
