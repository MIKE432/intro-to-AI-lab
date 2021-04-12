from copy import deepcopy
from typing import List

from Tools import remove_from_domain, init_queue_of_arcs, revise
from abstracts.Problem import Problem
from abstracts.Variable import Variable


def forward_checking(problem: Problem, current: Variable, removed):
    counter = 0
    for neighbour in current.neighbours:
        if not neighbour.is_value_changed():
            for value in deepcopy(neighbour.domain):
                neighbour.value = value
                if not problem.constraint(current, neighbour):
                    remove_from_domain(neighbour, value, removed)
                else:
                    counter += 1

            neighbour.to_empty()
            if counter == 0:
                return False
    return True


def AC3(problem: Problem, queue: List, removed):
    if queue is None:
        queue = []
        init_queue_of_arcs(problem, queue)

    while len(queue) != 0:
        Xi, Xj = queue.pop(0)
        if revise(problem, Xi, Xj, removed):
            if len(Xi.domain) == 0:
                return False

            for Xk in Xi.neighbours:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True


def mac(problem: Problem, current: Variable, removed):
    queue = []
    for Xk in current.neighbours:
        if not Xk.is_value_changed():
            queue.append((current, Xk))
    return AC3(problem, queue, removed)


# to pick next empty
def mrv(problem: Problem):
    sorted_nodes = sorted(filter(lambda _x: not _x.is_value_changed(), problem.nodes),
                          key=lambda _x: len(_x.domain))

    if len(sorted_nodes) == 0:
        return None
    return sorted_nodes[0]


# to pick next value from domain
def lcv(problem: Problem, current: Variable):
    c_s = []

    for value in current.domain:
        current.value = value
        s = sum(problem.number_of_conflicts())
        c_s.append((s, value))
        current.to_empty()

    return list(map(lambda _x: _x[1], sorted(c_s, key=lambda _x: _x[0])))
