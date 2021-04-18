from implementations.Consts import PLAYER_TWO, PLAYER_ONE


def get_opposite_index(index):
    indexes1 = [6, 5, 4, 3, 2, 1, 0]
    indexes2 = [6, 7, 8, 9, 10, 11, 12]
    if index in indexes1:
        return indexes1.index(index) * 2 + index
    else:
        return index - indexes2.index(index) * 2


def turn(board, current_player):
    another_turn = True
    while another_turn and not end_condition_mancala(board):
        player_choice = current_player.move(get_player_choices(board, current_player.tag), board)
        another_turn = move_chosen_pieces(board, current_player.tag, player_choice)


def end_condition_mancala(board):
    return sum(board[0:6]) == 0 or sum(board[7:13]) == 0


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
    for i in range(1, count + 1):
        current = (choice + i + incremented) % 14
        if current != invalid:

            if current in player_part and board[current] == 0 and i == count:
                opposite = get_opposite_index(current)
                if board[opposite] != 0:
                    move_from_to(board, current_player_tag, opposite, base, board[opposite], True)
                    move_from_to(board, current_player_tag, choice, base)
                else:
                    move_from_to(board, current_player_tag, choice, current)
            else:
                move_from_to(board, current_player_tag, choice, current)

            if i == count and current == base:
                another_turn = True
        else:
            move_from_to(board, current_player_tag, choice, (current + 1) % 14)
            incremented += 1

    return another_turn


def get_player_choices(board, current_player_tag):
    start, end = (0, 6) if current_player_tag == PLAYER_ONE else (7, 13)
    return list(filter(lambda _x: board[_x] != 0, list(range(start, end))))


def evaluate_function(board):
    player1 = board[6]
    player2 = board[13]

    return {
        PLAYER_ONE: player1,
        PLAYER_TWO: player2
    }
