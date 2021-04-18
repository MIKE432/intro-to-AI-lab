from implementations.Consts import PLAYER_ONE, PLAYER_TWO


def get_other_player(current_player_tag):
    players = [PLAYER_ONE, PLAYER_TWO]
    players.remove(current_player_tag)
    return players[0]