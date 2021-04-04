import math
from copy import deepcopy, copy
from random import randint
from typing import List

from Tools import intersect
from abstracts.Variable import Variable
from abstracts.Problem import Problem


def generate_map_coloring_problem(nodes_count: int, width: int, height: int, domain):
    problem = MapColoring(width, height, domain)
    points = []
    for i in range(0, nodes_count):
        while True:
            x = randint(0, width)
            y = randint(0, height)
            if (x, y) not in points:
                node = MapColoringNode(domain, x, y)
                problem.add_node(node)
                break

    find_neighbours(problem)

    return problem


def find_neighbours(problem):
    invalid_nodes = []
    while len(invalid_nodes) < len(problem.nodes):
        for node in problem.nodes:
            best_node = get_best_node(problem, node)
            if best_node is not None:
                node.add_neighbour(best_node)
            else:
                invalid_nodes.append(node)
                invalid_nodes = list(invalid_nodes)


def get_best_node(problem, node):
    min_distance = problem.width * problem.height
    best_node = None
    for other_node in problem.nodes:
        if other_node != node and other_node not in node.neighbours:
            connection = [node, other_node]
            if not is_connection_not_valid(connection, problem):
                a = other_node.x - node.x
                b = other_node.y - node.y
                distance = math.sqrt(a * a + b * b)
                if distance < min_distance:
                    min_distance = distance
                    best_node = other_node

    return best_node


def is_connection_not_valid(connection, problem):
    for node in problem.nodes:
        for neighbour in node.neighbours:
            if intersect((connection[0].x, connection[0].y), (connection[1].x, connection[1].y),
                         (neighbour.x, neighbour.y), (node.x, node.y)):
                if node not in connection and neighbour not in connection:
                    return True
    return False


class MapColoringNode(Variable):
    def __init__(self, domain: List, x: int, y: int, def_val=0):
        super().__init__(def_val, domain)
        self.neighbours = []
        self.x = x
        self.y = y

    def add_neighbour(self, node):
        if node in self.neighbours:
            return
        self.neighbours.append(node)
        node.neighbours.append(self)


class MapColoring(Problem):

    def __init__(self, width: int, height: int, domain):
        super().__init__(domain)
        self.width = width
        self.height = height
        self.domain = domain

    def next(self):
        return self.__find_next_empty_node()

    def add_node(self, node: MapColoringNode):
        self.nodes.append(node)

    def get_dims(self):
        return self.width, self.height

    def __find_next_empty_node(self):
        for i in range(0, len(self.nodes)):
            if not self.nodes[i].is_value_changed():
                return self.nodes[i]
        return None

    def get_positions(self):
        return list(map(lambda _x: (_x.x, _x.y), self.nodes))

    def get_connections_indexes(self):
        _indexes = []
        for node in self.nodes:
            indexes = []
            for neighbour in node.neighbours:
                indexes.append(self.nodes.index(neighbour))
            _indexes.append(indexes)

        return _indexes

    def get_node_colors(self):
        return list(map(lambda _x: _x.value, self.nodes))
