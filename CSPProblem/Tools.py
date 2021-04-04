import json
import math


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def create_json(problem):
    data = {'board': math.floor(problem.width * 1.5), 'regions': problem.get_positions(),
            'colors': problem.get_node_colors(),
            'connections': problem.get_connections_indexes()}
    to_json = json.loads(json.dumps(data, indent=4))
    return to_json


def create_map(problem):
    json_data = create_json(problem)
    with open('Generator/json_map.json', 'w') as file:
        json.dump(json_data, file)


def remove_from_domain(node, value, removed):
    node.domain.remove(value)
    removed.append((node, value))


def restore_nodes(removed):
    for node, value in removed:
        node.add_to_domain(value)
