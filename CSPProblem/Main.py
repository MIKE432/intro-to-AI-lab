from BackTracking import BackTracking
from EinsteinRiddle import EinsteinRiddle, init_einstein_problem
from MapColoring import generate_map_coloring_problem
from Tools import create_map
from constraint_functions.EinsteinRiddleConstraints import apply_einstein_constraints
from constraint_functions.MapColoringConstraints import node_constraint_map_coloring

if __name__ == "__main__":
    problem = generate_map_coloring_problem(20, 40, 40, [1, 2, 3, 4, 5, 6])
    # problem = init_einstein_problem()
    # apply_einstein_constraints(problem)
    problem.add_constraint(node_constraint_map_coloring)
    resolver = BackTracking(problem)
    resolver.resolve_problem()

    create_map(problem)
