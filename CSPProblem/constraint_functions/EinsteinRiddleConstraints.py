from EinsteinConsts import *
from EinsteinRiddle import EinsteinVariable, EinsteinRiddle


def check_type(variable):
    return int(variable.about / 10)


def are_different(node1: EinsteinVariable, node2: EinsteinVariable):
    if node1.value == -1 and node2.value == -1:
        return True

    if are_types_the_same(node1, node2):
        return node1.value != node2.value

    return True


def are_types_the_same(node1: EinsteinVariable, node2: EinsteinVariable):
    return check_type(node1) == check_type(node2)


def constraint(node1: EinsteinVariable, node2: EinsteinVariable):
    if not node1.is_value_changed() or not node2.is_value_changed():
        return True

    if are_types_the_same(node1, node2):
        # 3
        if node1.about == COLOR_GREEN and node2.about == COLOR_WHITE:
            return node1.value + 1 == node2.value
        elif node2.about == COLOR_GREEN and node1.about == COLOR_WHITE:
            return node1.value - 1 == node2.value

        return are_different(node1, node2)

    # 5
    if node1.about == SMOKE_LIGHT and node2.about == PET_CATS:
        return node2.value in [node1.value - 1, node1.value + 1]
    elif node2.about == SMOKE_LIGHT and node1.about == PET_CATS:
        return node1.value in [node2.value - 1, node2.value + 1]

    # 9
    if node1.about == SMOKE_LIGHT and node2.about == DRINK_WATER:
        return node2.value in [node1.value - 1, node1.value + 1]
    elif node2.about == SMOKE_LIGHT and node1.about == DRINK_WATER:
        return node1.value in [node2.value - 1, node2.value + 1]

    # 12
    if node1.about == NATIONALITY_NORWEGIAN and node2.about == COLOR_BLUE:
        return node2.value in [node1.value - 1, node1.value + 1]
    elif node2.about == NATIONALITY_NORWEGIAN and node1.about == COLOR_BLUE:
        return node1.value in [node2.value - 1, node2.value + 1]

    # 13
    if node1.about == PET_HORSES and node2.about == COLOR_YELLOW:
        return node2.value in [node1.value - 1, node1.value + 1]
    elif node2.about == PET_HORSES and node1.about == COLOR_YELLOW:
        return node1.value in [node2.value - 1, node2.value + 1]

    # need to be the same when checking normal constraint
    return node1.value == node2.value


def print_einstein(problem: EinsteinRiddle):
    for i in range(0, 5):
        print("Domek" + str(i))
        nodes_per_house = list(filter(lambda _x: _x.value == i, problem.nodes))
        for node in nodes_per_house:
            print(node.about)
