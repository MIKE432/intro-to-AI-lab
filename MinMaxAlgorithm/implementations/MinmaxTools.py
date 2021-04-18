def min_max(node, depth, maximizing_player, end_condition, evaluate):
    if depth == 0 or end_condition(node.board):
        return evaluate(node.board)[node.player_tag]

    if maximizing_player == node.player_tag:
        max_eval = -100000000
        node.value = -100000000
        for child in node.children:
            eval = min_max(child, depth - 1, maximizing_player, end_condition, evaluate)
            max_eval = max(max_eval, eval)
            node.value = max_eval
        return max_eval
    else:
        min_eval = 100000000
        node.value = 100000000
        for child in node.children:
            eval = min_max(child, depth - 1, maximizing_player, end_condition, evaluate)
            min_eval = min(min_eval, eval)
            node.value = min_eval
        return min_eval

