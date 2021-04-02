from random import randint
from typing import List

from abstracts.Problem import Problem
from abstracts.Variable import Variable


def init_einstein_problem():
    problem = EinsteinRiddle([0, 1, 2, 3, 4])
    for i in range(0, 5):
        problem.add_node(EinsteinRiddleNode([-1, -1, -1, -1, -1], problem.domain))

    return problem


class EinsteinRiddleNode(Variable):
    def __init__(self, def_val, domain: List):
        super().__init__(def_val, domain)
        self.__next_empty = 0

    def pick_random_value(self, predefined=None):
        if predefined is not None:
            self.value[self.__next_empty] = predefined
        else:
            self.value[self.__next_empty] = randint(0, len(self.domain))

        self.__next_empty += 1

    def to_empty(self):
        self.__next_empty -= 1
        self.value[self.__next_empty] = self.def_val[self.__next_empty]

    def is_value_changed(self):
        return self.__next_empty == len(self.value)


class EinsteinRiddle(Problem):
    def __init__(self, domain):
        super().__init__(domain)
        self.__prev = 0

    def next(self):
        return self.__find_next_empty_node()

    def __find_next_empty_node(self):
        for i in range(self.__prev % len(self.nodes), len(self.nodes)):
            if not self.nodes[i].is_value_changed():
                return self.nodes[i]
        return None
