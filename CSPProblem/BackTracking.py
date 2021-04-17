from Consts import FORWARD_CHECKING
from Heuristics import forward_checking, mrv, lcv, mac
from Tools import restore_nodes
from abstracts.Problem import Problem
from abstracts.Resolver import Resolver
from abstracts.default_functions import no_checking, no_sort, overridden_next


class BackTracking(Resolver):
    def __init__(self, problem: Problem):
        super().__init__(problem)
        self.solutions = []
        self.n = 0

    def resolve_problem(self, picking_next_heuristics=overridden_next, evaluate=no_checking, sort_values=no_sort):
        return self.__backtrack(picking_next_heuristics, evaluate, sort_values)

    def accept(self):
        return sum(self.problem.number_of_conflicts()) == 0

    def reset(self):
        self.n = 0

    def __backtrack(self, picking_next_heuristics, evaluate, sort_values):
        next_empty = picking_next_heuristics(self.problem)
        if next_empty is None:
            return True

        for val in sort_values(self.problem, next_empty):
            next_empty.pick_random_value(val)  # setter
            self.n += 1
            removed = []
            if self.accept():
                if evaluate(self.problem, next_empty, removed):
                    if self.__backtrack(picking_next_heuristics, evaluate, sort_values):
                        return True
            restore_nodes(removed)
            next_empty.to_empty()

        return False
