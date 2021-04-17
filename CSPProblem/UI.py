import matplotlib.pyplot as plt

from Heuristics import mac, forward_checking, lcv, mrv
from abstracts.default_functions import no_checking, no_sort, overridden_next


def get_alg_name(alg):
    if alg == no_checking:
        return "Default Backtracking"
    elif alg == mac:
        return "AC-3"
    elif alg == forward_checking:
        return "Forward checking"


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


def get_alg_name_by_number(num):
    if num == 0:
        return "Default Backtracking"
    elif num == 2:
        return "AC-3"
    elif num == 1:
        return "Forward checking"


def get_heuristic_name(h1, h2):
    if h1 == lcv and h2 == mrv:
        return "MRV+LCV"

    if h1 == lcv and h2 is overridden_next:
        return "LCV"

    if h1 is no_sort and h2 == mrv:
        return "MRV"

    return "Brak"
