from copy import deepcopy

import numpy as np

from Tools import get_other_player
from implementations.MancalaDecisionTree import MancalaDecisionNode
from implementations.MancalaTools import get_player_choices, move_chosen_pieces


def min_max(node, depth, maximizing_player, end_condition, evaluate, alpha, beta):
    if depth == 0 or end_condition(node.board):
        return evaluate(node.board)[node.player_tag]

    if maximizing_player == node.player_tag:
        max_eval = np.inf * -1
        node.value = np.inf * -1
        for child in node.children:
            eval = min_max(child, depth - 1 if child.player_tag != node.player_tag else depth, maximizing_player,
                           end_condition, evaluate, alpha, beta)
            max_eval = max(max_eval, eval)
            node.value = max_eval
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval
    else:
        min_eval = np.inf
        node.value = np.inf
        for child in node.children:
            eval = min_max(child, depth - 1 if child.player_tag != node.player_tag else depth, maximizing_player,
                           end_condition, evaluate, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            node.value = min_eval
            if beta <= alpha:
                break
        return min_eval


def min_max2(board, player_tag, depth, maximizing_player, end_condition, evaluate, alpha, beta):
    if depth == 0 or end_condition(board):
        return evaluate(board)[maximizing_player]

    if maximizing_player == player_tag:
        max_eval = np.inf * -1
        for choice in get_player_choices(board, player_tag):
            new_board = deepcopy(board)
            another_turn = move_chosen_pieces(new_board, player_tag, choice)

            eval = min_max2(new_board, get_other_player(
                player_tag) if not another_turn else player_tag, depth - 1 if not another_turn else depth,
                           maximizing_player,
                           end_condition, evaluate, alpha, beta)
            max_eval = max(max_eval, eval)

            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = np.inf
        for choice in get_player_choices(board, player_tag):
            new_board = deepcopy(board)
            another_turn = move_chosen_pieces(new_board, player_tag, choice)

            eval = min_max2(new_board, get_other_player(
                player_tag) if not another_turn else player_tag, depth - 1 if not another_turn else depth,
                            maximizing_player,
                            end_condition, evaluate, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


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
