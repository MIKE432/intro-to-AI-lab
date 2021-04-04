from random import randint
from typing import List

from abstracts.Problem import Problem
from abstracts.Variable import Variable


def init_einstein_problem():
    problem = EinsteinRiddle([0, 1, 2, 3, 4])
    for i in range(0, 5):
        for j in range(0, 5):
            problem.add_node(Variable(-1, problem.domain))

    return problem


class EinsteinRiddle(Problem):
    def __init__(self, domain):
        super().__init__(domain)
        self.__prev = 0

    def next(self):
        return self.__find_next_empty_node()

    def __find_next_empty_node(self):
        for i in range(0, len(self.nodes)):
            if not self.nodes[i].is_value_changed():
                return self.nodes[i]
        return None

    def number_of_conflicts(self):
        nodes = wrap_variables(self.nodes)
        counter = [0 for _ in nodes]

        for constraint in self.constraints:
            for i in range(0, len(nodes)):
                if not constraint(nodes[i]):
                    counter[i] += 1
        return counter


class EinsteinRiddleNodeWrapper:
    def __init__(self, node_id):
        self.node_id = node_id
        self.value = []
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)


def wrap_variables(variables: List):
    _vars = []
    _id = 0

    values = []
    for i in range(0, 5):
        values.append(list(map(lambda _x: _x.value, variables[i * 5:5 * (i + 1)])))

    for i in range(0, 5):
        _vars.append(EinsteinRiddleNodeWrapper(i))

    for i in range(0, 5):
        _vars[i].value = values[i]

    for i in range(0, 5):
        for j in range(0, 5):
            if i != j:
                _vars[i].add_neighbour(_vars[j])

    return _vars
