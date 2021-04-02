from typing import List


def node_constraint_map_coloring(nodes: List):
    for node in nodes:
        for neighbour in node.neighbours:
            if neighbour.value == node.value and neighbour.is_value_changed():
                return False
    return True
