from statistics import mean

from BackTracking import BackTracking
from Consts import FORWARD_CHECKING, NORMAL
from EinsteinRiddle import EinsteinRiddle, init_einstein_problem
from MapColoring import generate_map_coloring_problem
from Tools import create_map
from constraint_functions.EinsteinRiddleConstraints import constraint, print_einstein
from constraint_functions.MapColoringConstraints import node_constraint_map_coloring

if __name__ == "__main__":
    problem = init_einstein_problem()
    problem.constraint = constraint
    # apply_einstein_constraints(problem)
    # problem = generate_map_coloring_problem(20, 40, 40, [1, 2, 3, 4])
    # problem.add_constraint(node_constraint_map_coloring)

    resolver = BackTracking(problem)
    resolver.resolve_problem(FORWARD_CHECKING)

    print(list(map(lambda _x: _x.value, problem.nodes)))
    print_einstein(problem)

    # res.append(resolver.n)
    # res = []
    # for i in range(0, 50):
    #
    #
    # print(mean(res))
    # print(res)

    # for node in problem.nodes:
    #     print(node.value)
    # create_map(problem)
