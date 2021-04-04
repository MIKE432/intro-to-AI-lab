from typing import List

from EinsteinRiddle import EinsteinRiddleNodeWrapper
from abstracts.Problem import Problem


def hint1(node: EinsteinRiddleNodeWrapper):
    if node.node_id == 0:
        return node.value[1] in [-1, 0]
    return True


def hint2(node: EinsteinRiddleNodeWrapper):
    if node.value[0] == 0:
        return node.value[1] in [-1, 1]
    if node.value[1] == 1:
        return node.value[0] in [-1, 0]

    return True


def hint3(node: EinsteinRiddleNodeWrapper):
    if node.value[0] == 1:
        node_right = get_node_by_id(node.neighbours, node.node_id + 1)
        if node_right is None:
            return False
        return node_right.value[0] in [-1, 4]

    if node.value[0] == 4:
        node_left = get_node_by_id(node.neighbours, node.node_id - 1)
        if node_left is None:
            return False
        return node_left.value[0] in [-1, 1]

    return True


def hint4(node: EinsteinRiddleNodeWrapper):
    if node.value[1] == 2:
        return node.value[3] in [-1, 0]

    if node.value[3] == 0:
        return node.value[1] in [-1, 2]

    return True


def hint5(node: EinsteinRiddleNodeWrapper):
    if node.value[2] == 0:
        node_left = get_node_by_id(node.neighbours, node.node_id - 1)
        node_right = get_node_by_id(node.neighbours, node.node_id + 1)
        if node_left is not None and node_right is not None:
            return node_left.value[4] in [-1, 0] or node_right.value[3] in [-1, 2]
        elif node_left is not None:
            return node_left.value[4] in [-1, 0]
        else:
            return node_right.value[4] in [-1, 0]

    return True


def hint6(node: EinsteinRiddleNodeWrapper):
    if node.value[0] == 2:
        return node.value[2] in [-1, 1]

    if node.value[2] == 1:
        return node.value[0] in [-1, 2]
    return True


def hint7(node: EinsteinRiddleNodeWrapper):
    if node.value[1] == 3:
        return node.value[2] in [-1, 2]

    if node.value[2] == 2:
        return node.value[1] in [-1, 3]

    return True


def hint8(node: EinsteinRiddleNodeWrapper):
    if node.node_id == 2:
        return node.value[3] in [-1, 1]
    return True


def hint9(node: EinsteinRiddleNodeWrapper):
    if node.value[2] == 0:
        node_left = get_node_by_id(node.neighbours, node.node_id - 1)
        node_right = get_node_by_id(node.neighbours, node.node_id + 1)
        if node_left is not None and node_right is not None:
            return node_left.value[3] in [-1, 2] or node_right.value[3] in [-1, 2]
        elif node_left is not None:
            return node_left.value[3] in [-1, 2]
        else:
            return node_right.value[3] in [-1, 2]

    return True


def hint10(node: EinsteinRiddleNodeWrapper):
    if node.value[2] == 3:
        return node.value[4] in [-1, 1]

    if node.value[4] == 1:
        return node.value[2] in [-1, 3]

    return True


def hint11(node: EinsteinRiddleNodeWrapper):
    if node.value[1] == 4:
        return node.value[4] in [-1, 2]

    if node.value[4] == 2:
        return node.value[1] in [-1, 4]

    return True


def hint12(node: EinsteinRiddleNodeWrapper):
    if node.value[1] == 0:
        node_left = get_node_by_id(node.neighbours, node.node_id - 1)
        node_right = get_node_by_id(node.neighbours, node.node_id + 1)
        if node_left is not None and node_right is not None:
            return node_left.value[0] in [-1, 3] or node_right.value[0] in [-1, 3]
        elif node_left is not None:
            return node_left.value[0] in [-1, 3]
        else:
            return node_right.value[0] in [-1, 3]

    return True


def hint13(node: EinsteinRiddleNodeWrapper):
    if node.value[4] == 3:
        node_left = get_node_by_id(node.neighbours, node.node_id - 1)
        node_right = get_node_by_id(node.neighbours, node.node_id + 1)
        if node_left is not None and node_right is not None:
            return node_left.value[0] in [-1, 2] or node_right.value[0] in [-1, 2]
        elif node_left is not None:
            return node_left.value[0] in [-1, 2]
        else:
            return node_right.value[0] in [-1, 2]

    return True


def hint14(node: EinsteinRiddleNodeWrapper):
    if node.value[2] == 4:
        return node.value[3] in [-1, 3]

    if node.value[3] == 3:
        return node.value[2] in [-1, 3]

    return True


def hint15(node: EinsteinRiddleNodeWrapper):
    if node.value[0] == 1:
        return node.value[3] in [-1, 4]

    if node.value[3] == 4:
        return node.value[0] in [-1, 1]

    return True


def no_duplicate_constraint(node: EinsteinRiddleNodeWrapper):
    for neighbour in node.neighbours:
        for i in range(0, len(node.value)):
            if neighbour.value[i] == node.value[i]:
                if neighbour.value[i] != -1:
                    return False

    return True


def get_node_by_id(neighbours, node_id):
    l = list(filter(lambda _x: _x.node_id == node_id, neighbours))
    if len(l) == 0:
        return None

    return l[0]


def apply_einstein_constraints(problem: Problem):
    problem.add_constraint(hint1)
    problem.add_constraint(hint2)
    problem.add_constraint(hint3)
    problem.add_constraint(hint4)
    problem.add_constraint(hint5)
    problem.add_constraint(hint6)
    problem.add_constraint(hint7)
    problem.add_constraint(hint8)
    problem.add_constraint(hint9)
    problem.add_constraint(hint10)
    problem.add_constraint(hint11)
    problem.add_constraint(hint12)
    problem.add_constraint(hint13)
    problem.add_constraint(hint14)
    problem.add_constraint(hint15)
    problem.add_constraint(no_duplicate_constraint)
