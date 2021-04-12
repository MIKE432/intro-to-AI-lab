from typing import List
from abstracts.Variable import Variable
from abstracts.default_functions import no_constraint


class Problem:
    # constraints are functions that applies to specific/all nodes by passing node/all nodes as a parameter
    def __init__(self, domain):
        self.nodes = []
        self.domain = domain
        self.constraint = no_constraint

    def apply_nodes(self, nodes: List):
        self.nodes = nodes

    def add_constraint(self, constraint):
        self.constraint = constraint

    def number_of_conflicts(self):
        counter = [0 for _ in self.nodes]

        for i in range(0, len(self.nodes)):
            counter[i] += self.__get_number_of_inconsistency(i)

        return counter

    def __get_number_of_inconsistency(self, i):
        counter = 0
        for neighbour in self.nodes[i].neighbours:
            counter += 0 if self.constraint(self.nodes[i], neighbour) else 1

        return counter

    def next(self):
        pass

    def add_node(self, node: Variable):
        self.nodes.append(node)

    def evaluate_domain(self):
        pass

    def __str__(self):
        return str(list(map(lambda _x: str(_x), self.nodes)))
