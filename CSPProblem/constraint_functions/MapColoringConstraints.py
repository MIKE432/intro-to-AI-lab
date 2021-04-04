from MapColoring import MapColoringNode


def node_constraint_map_coloring(node: MapColoringNode, neighbour: MapColoringNode):
    return neighbour.value != node.value or not neighbour.is_value_changed()
