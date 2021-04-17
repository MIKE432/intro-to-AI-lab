from datetime import datetime
from statistics import mean
from time import time

from BackTracking import BackTracking
from Consts import FORWARD_CHECKING, NORMAL
from EinsteinRiddle import EinsteinRiddle, init_einstein_problem
from Heuristics import lcv, mrv, forward_checking, mac
from MapColoring import generate_map_coloring_problem
from UI import get_alg_name, create_plot, get_alg_name_by_number, get_heuristic_name
from abstracts.default_functions import no_sort, no_checking, overridden_next
from constraint_functions.EinsteinRiddleConstraints import constraint, print_einstein
from constraint_functions.MapColoringConstraints import node_constraint_map_coloring


def calculate_time_millis(f, **kwargs):
    start = int(time() * 1000)
    res = f(**kwargs)
    end = int(time() * 1000)
    return end - start, res


if __name__ == "__main__":
    value_heuristics = [no_sort, lcv]
    variable_heuristics = [overridden_next, mrv]
    constraint_domain_algorithms = [no_checking, forward_checking, mac]
    with_checking = 20, 140
    without_checking = 5, 45

    # time_plot = {
    #     "Default Backtracking": [],
    #     "AC-3": [],
    #     "Forward checking": [],
    #     "x": []
    # }
    #
    # nodes_visited_plot = {
    #     "Default Backtracking": [],
    #     "AC-3": [],
    #     "Forward checking": [],
    #     "x": []
    # }
    #
    # for i in range(2, 20):
    #     res_millis = [[], [], []]
    #     res_visit = [[], [], []]
    #     print(i)
    #     for j in range(0, 50):
    #         problem = generate_map_coloring_problem(i, 190, 190, [1, 2, 3, 4, 5])
    #         problem.add_constraint(node_constraint_map_coloring)
    #         resolver = BackTracking(problem)
    #         for evaluate in constraint_domain_algorithms:
    #             name = get_alg_name(evaluate)
    #             millis, found = 0, False
    #             while not found:
    #                 millis, found = calculate_time_millis(resolver.resolve_problem,
    #                                                       picking_next_heuristics=overridden_next,
    #                                                       evaluate=evaluate,
    #                                                       sort_values=no_sort)
    #             res_millis[constraint_domain_algorithms.index(evaluate)].append(millis)
    #             res_visit[constraint_domain_algorithms.index(evaluate)].append(resolver.n)
    #
    #             problem.reset()
    #             resolver.reset()
    #
    #     time_plot[get_alg_name_by_number(0)].append(mean(res_millis[0]))
    #     time_plot[get_alg_name_by_number(1)].append(mean(res_millis[1]))
    #     time_plot[get_alg_name_by_number(2)].append(mean(res_millis[2]))
    #
    #     nodes_visited_plot[get_alg_name_by_number(0)].append(mean(res_visit[0]))
    #     nodes_visited_plot[get_alg_name_by_number(1)].append(mean(res_visit[1]))
    #     nodes_visited_plot[get_alg_name_by_number(2)].append(mean(res_visit[2]))
    #
    #     time_plot["x"].append(i)
    #     nodes_visited_plot["x"].append(i)
    #
    # create_plot(time_plot, "Algorytmy", "Wielkość mapy", "Czas", "assets/mapa_algorytmy_czas.png")
    # create_plot(nodes_visited_plot, "Algorytmy", "Wielkość mapy", "Ilość odwiedzonych nodów", "assets/mapa_algorytmy_nody.png")
    # ----------------------------------------------------------------------
    # porównianie heurystyk
    #
    # time_plot = {
    #     "MRV": [],
    #     "LCV": [],
    #     "Brak": [],
    #     "MRV+LCV": [],
    #     "x": []
    # }
    #
    # nodes_visited_plot = {
    #     "MRV": [],
    #     "LCV": [],
    #     "Brak": [],
    #     "MRV+LCV": [],
    #     "x": []
    # }
    #
    # for i in range(2, 40):
    #     print(i)
    #     res_millis = {
    #         (no_sort, overridden_next): [],
    #         (lcv, overridden_next): [],
    #         (no_sort, mrv): [],
    #         (lcv, mrv): []
    #     }
    #     res_visit = {
    #         (no_sort, overridden_next): [],
    #         (lcv, overridden_next): [],
    #         (no_sort, mrv): [],
    #         (lcv, mrv): []
    #     }
    #
    #     for j in range(0, 30):
    #         problem = generate_map_coloring_problem(i, 190, 190, [1, 2, 3, 4, 5])
    #         problem.add_constraint(node_constraint_map_coloring)
    #         resolver = BackTracking(problem)
    #         for h1 in value_heuristics:
    #             for h2 in variable_heuristics:
    #                 millis, found = 0, False
    #                 while not found:
    #                     millis, found = calculate_time_millis(resolver.resolve_problem,
    #                                                           picking_next_heuristics=h2,
    #                                                           evaluate=forward_checking,
    #                                                           sort_values=h1)
    #
    #                 res_millis[(h1, h2)].append(millis)
    #                 res_visit[(h1, h2)].append(resolver.n)
    #                 problem.reset()
    #                 resolver.reset()
    #
    #     for h1, h2 in res_millis.keys():
    #         time_plot[get_heuristic_name(h1, h2)].append(mean(res_millis[(h1, h2)]))
    #
    #
    #     for h1, h2 in res_visit.keys():
    #         nodes_visited_plot[get_heuristic_name(h1, h2)].append(mean(res_visit[(h1, h2)]))
    #
    #     time_plot["x"].append(i)
    #     nodes_visited_plot["x"].append(i)
    #
    # create_plot(time_plot, "Heurystyki",  "Wielkość mapy", "Czas", "assets/mapa_heurystyki_czas.png")
    # create_plot(nodes_visited_plot, "Heurystyki", "Ilość odwiedzonych nodów", "Wielkość mapy",
    #             "assets/mapa_heurystyki_nody.png")
    #


#     ---------------------------------------------------------------------------
# einstein

    problem = init_einstein_problem()
    resolver = BackTracking(problem)
    problem.add_constraint(constraint)

    result = []
    # print(calculate_time_millis(resolver.resolve_problem, picking_next_heuristics=overridden_next, evaluate=no_checking, sort_values=no_sort))
    print(datetime.fromtimestamp(1347829215))
    for evaluate in constraint_domain_algorithms:
        evaluate_result = []
        for h1 in value_heuristics:
            h1_result = []
            for h2 in variable_heuristics:
                millis, found = calculate_time_millis(resolver.resolve_problem, picking_next_heuristics=h2, evaluate=evaluate, sort_values=h1)
                h1_result.append((millis, resolver.n))
                problem.reset()
                resolver.reset()

            evaluate_result.append(h1_result)
        result.append(evaluate_result)

    print(result)