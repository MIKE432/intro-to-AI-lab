from copy import deepcopy

from Tools import get_other_player
from implementations.MancalaTools import get_player_choices, move_chosen_pieces


def apply_decision_tree_to_root(curr_board, current_node, depth):
    if depth == 0:
        return
    for choice in get_player_choices(curr_board, current_node.player_tag):
        new_board = deepcopy(curr_board)
        another_turn = move_chosen_pieces(new_board, current_node.player_tag, choice)
        node = MancalaDecisionNode(new_board, current_node.player_tag if another_turn else get_other_player(
            current_node.player_tag), choice)
        current_node.add_child(node)
        apply_decision_tree_to_root(new_board, node, depth - 1 if not another_turn else depth)


class MancalaDecisionNode:
    def __init__(self, board, player_tag, after_picking):
        self.board = deepcopy(board)
        self.children = []
        self.player_tag = player_tag
        self.after_picking = after_picking
        self.value = 0

    def add_child(self, other_node):
        self.children.append(other_node)
