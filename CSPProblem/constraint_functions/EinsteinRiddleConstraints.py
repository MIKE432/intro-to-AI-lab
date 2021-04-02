from typing import List

from EinsteinRiddle import EinsteinRiddleNode
from abstracts.Problem import Problem


def hint1(node: EinsteinRiddleNode):
    return node.value[1] in [-1, 0]


def hint2(nodes: List):
    for node in nodes:
        if node.value[0] == 0:
            return node.value[1] in [-1, 1]

        if node.value[1] == 1:
            return node.value[0] in [-1, 0]
    return True


def hint3(nodes: List):
    for i in range(len(nodes)):
        if nodes[i].value[0] == 1:
            if i == len(nodes) - 1:
                return False

            return nodes[i + 1].value[0] in [-1, 4]

        if nodes[i].value[0] == 4:
            if i == 0:
                return False

            return nodes[i - 1].value[0] in [-1, 1]
    return True


def hint4(nodes: List):
    for node in nodes:
        if node.value[1] == 2:
            return node.value[3] in [-1, 0]

        if node.value[3] == 0:
            return node.value[1] in [-1, 2]
    return True


def hint5(nodes: List):
    for i in range(len(nodes)):
        if nodes[i].value[2] == 0:
            if 0 < i < len(nodes) - 1:
                return (nodes[i - 1].value[4] in [-1, 0]) or (nodes[i + 1].value[4] in [-1, 0])
            elif i == 0:
                return nodes[i + 1].value[4] in [-1, 0]
            elif i == len(nodes) - 1:
                return nodes[i - 1].value[4] in [-1, 0]
    return True


def hint6(nodes: List):
    for node in nodes:
        if node.value[0] == 2:
            return node.value[2] in [-1, 1]

        if node.value[2] == 1:
            return node.value[0] in [-1, 2]
    return True


def hint7(nodes: List):
    for node in nodes:
        if node.value[1] == 3:
            return node.value[2] in [-1, 2]

        if node.value[2] == 2:
            return node.value[1] in [-1, 3]
    return True


def hint8(node: EinsteinRiddleNode):
    return node.value[3] in [-1, 1]


def hint9(nodes: List):
    for i in range(len(nodes)):
        if nodes[i].value[2] == 0:
            if 0 < i < len(nodes) - 1:
                return (nodes[i - 1].value[3] in [-1, 2]) or (nodes[i + 1].value[3] in [-1, 2])
            elif i == 0:
                return nodes[i + 1].value[3] in [-1, 2]
            elif i == len(nodes) - 1:
                return nodes[i - 1].value[3] in [-1, 2]
    return True


def hint10(nodes: List):
    for node in nodes:
        if node.value[2] == 3:
            return node.value[4] in [-1, 1]

        if node.value[4] == 1:
            return node.value[2] in [-1, 3]
    return True


def hint11(nodes: List):
    for node in nodes:
        if node.value[1] == 4:
            return node.value[4] in [-1, 2]

        if node.value[4] == 2:
            return node.value[1] in [-1, 4]
    return True


def hint12(nodes: List):
    for i in range(len(nodes)):
        if nodes[i].value[1] == 0:
            if 0 < i < len(nodes) - 1:
                return (nodes[i - 1].value[0] in [-1, 3]) or (nodes[i + 1].value[0] in [-1, 3])
            elif i == 0:
                return nodes[i + 1].value[0] in [-1, 3]
            elif i == len(nodes) - 1:
                return nodes[i - 1].value[0] in [-1, 3]
    return True


def hint13(nodes: List):
    for i in range(len(nodes)):
        if nodes[i].value[4] == 3:
            if 0 < i < len(nodes) - 1:
                return (nodes[i - 1].value[0] in [-1, 2]) or (nodes[i + 1].value[0] in [-1, 2])
            elif i == 0:
                return nodes[i + 1].value[0] in [-1, 2]
            elif i == len(nodes) - 1:
                return nodes[i - 1].value[0] in [-1, 2]
    return True


def hint14(nodes: List):
    for node in nodes:
        if node.value[2] == 4:
            return node.value[3] in [-1, 3]

        if node.value[3] == 3:
            return node.value[2] in [-1, 3]
    return True


def hint15(nodes: List):
    for node in nodes:
        if node.value[0] == 1:
            return node.value[3] in [-1, 4]

        if node.value[3] == 4:
            return node.value[0] in [-1, 1]

    return True


def no_duplicate_constraint(nodes: List):
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            if i != j:
                for k in range(0, len(nodes[i].value)):
                    if nodes[i].value[k] != -1:
                        if nodes[i].value[k] == nodes[j].value[k]:
                            return False

    return True


def apply_einstein_constraints(problem: Problem):
    problem.add_node_specific_constraint(0, hint1)
    problem.add_constraint(hint2)
    problem.add_constraint(hint3)
    problem.add_constraint(hint4)
    problem.add_constraint(hint5)
    problem.add_constraint(hint6)
    problem.add_constraint(hint7)
    problem.add_node_specific_constraint(2, hint8)
    problem.add_constraint(hint9)
    problem.add_constraint(hint10)
    problem.add_constraint(hint11)
    problem.add_constraint(hint12)
    problem.add_constraint(hint13)
    problem.add_constraint(hint14)
    problem.add_constraint(hint15)
    problem.add_constraint(no_duplicate_constraint)
