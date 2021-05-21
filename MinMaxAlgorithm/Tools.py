from implementations.Consts import PLAYER_ONE, PLAYER_TWO
import matplotlib.pyplot as plt


def get_other_player(current_player_tag):
    players = [PLAYER_ONE, PLAYER_TWO]
    players.remove(current_player_tag)
    return players[0]


def create_plot(d, title, xlabel, ylabel, destination):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for key in d.keys():
        if key != "x":
            plt.plot(d["x"], d[key], label=key)

    plt.legend()
    plt.savefig(destination)
    plt.clf()
