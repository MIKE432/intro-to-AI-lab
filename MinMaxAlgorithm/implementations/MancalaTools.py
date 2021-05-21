from implementations.Consts import PLAYER_TWO, PLAYER_ONE


def get_opposite_index(index):
    indexes1 = [6, 5, 4, 3, 2, 1, 0]
    indexes2 = [6, 7, 8, 9, 10, 11, 12]
    if index in indexes1:
        return indexes1.index(index) * 2 + index
    else:
        return index - indexes2.index(index) * 2


def turn(board, current_player, is_first_turn=False):
    another_turn = True
    while another_turn and not end_condition_mancala(board):
        player_choice = current_player.move(get_player_choices(board, current_player.tag), board, is_first_turn)
        another_turn = move_chosen_pieces(board, current_player.tag, player_choice)


def end_condition_mancala(board):
    return sum(board[0:6]) == 0 or sum(board[7:13]) == 0 or board[6] > 24 or board[13] > 24


def get_end_condition_by_player(board, player_tag):
    if player_tag == PLAYER_ONE:
        return sum(board[0:6]) == 0
    if player_tag == PLAYER_TWO:
        return sum(board[7:13]) == 0

    return False


def move_from_to(board, player_tag, from_i, to_i, number=1, raw=False):
    if not raw:
        validate_indexes(player_tag, from_i, to_i)
        validate_number(board, from_i, number)

    board[from_i] -= number
    board[to_i] += number


def validate_indexes(player_tag, from_i, to_i):
    possible_choices = list(range(0, 14))
    to_remove = 13 if player_tag == PLAYER_ONE else 6
    possible_choices.remove(to_remove)

    if from_i not in possible_choices:
        raise IndexError(f"From index is not acceptable: {from_i}")

    if to_i not in possible_choices:
        raise IndexError(f"To index is not acceptable: {to_i}")

    return True


def validate_number(board, from_i, number):
    if not board[from_i] >= number:
        raise OverflowError(f"Cannot move {number} pieces from bracket where is only {board[from_i]} pieces")
    return True


def move_chosen_pieces(board, current_player_tag, choice):
    count = board[choice]
    invalid, base, player_part = (13, 6, list(range(0, 6))) if current_player_tag == PLAYER_ONE else (
        6, 13, list(range(7, 13)))
    incremented = 0
    another_turn = False
    after_beating = False
    for i in range(1, count + 1):
        current = (choice + i + incremented) % 14
        if current != invalid:

            if current in player_part and board[current] == 0 and i == count:
                opposite = get_opposite_index(current)
                if board[opposite] != 0:
                    move_from_to(board, current_player_tag, opposite, base, board[opposite], True)
                    move_from_to(board, current_player_tag, choice, base)
                    after_beating = True
                else:
                    move_from_to(board, current_player_tag, choice, current)
            else:
                move_from_to(board, current_player_tag, choice, current)

            if i == count and current == base:
                another_turn = True
        else:
            move_from_to(board, current_player_tag, choice, (current + 1) % 14)
            incremented += 1

    return another_turn and not after_beating


def get_player_choices(board, current_player_tag):
    start, end = (0, 6) if current_player_tag == PLAYER_ONE else (7, 13)
    return list(filter(lambda _x: board[_x] != 0, list(range(start, end))))


def evaluate_function(board):
    player1 = board[6]
    player2 = board[13]
    p1, _ = bonus_beating_enemy(player1, player2)
    _, p2 = combine_heuristics(board, player1, player2)
    return {
        PLAYER_ONE: p1,
        PLAYER_TWO: p2
    }


# heuristics
def bonus_endgame(board, p1, p2):
    exp = 0.8 if not end_condition_mancala(board) else 2
    p1 += sum(board[:6]) * exp
    p2 += sum(board[7:13]) * exp
    return p1, p2


def bonus_beating_enemy(p1, p2):
    return p1 - p2, p2 - p1


def no_heuristics(board):
    p1 = board[6]
    p2 = board[13]
    return p1, p2


def combine_heuristics(board, player1, player2):
    p1, p2 = bonus_endgame(board, player1, player2)
    p1_1, p2_1 = bonus_beating_enemy(player1, player2)

    return p1 + p1_1, p2 + p2_1
