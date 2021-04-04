from Consts import FORWARD_CHECKING
from Heuristics import forward_checking
from Tools import restore_nodes
from abstracts.Problem import Problem
from abstracts.Resolver import Resolver
from abstracts.default_functions import no_checking


class BackTracking(Resolver):
    def __init__(self, problem: Problem):
        super().__init__(problem)
        self.solutions = []
        self.n = 0

    def resolve_problem(self, type):
        if type == FORWARD_CHECKING:
            return self.backtrack(None, forward_checking)
        else:
            return self.backtrack(None, no_checking)

    def accept(self):
        return sum(self.problem.number_of_conflicts()) == 0

    def backtrack(self, heuristics=None, evaluate=no_checking):
        next_empty = self.problem.next()
        if next_empty is None:
            return True

        for val in next_empty.domain:
            next_empty.pick_random_value(val)
            removed = []
            if self.accept():
                if evaluate(self.problem, next_empty, removed):
                    if self.backtrack(heuristics, evaluate):
                        return True
            restore_nodes(removed)
            next_empty.to_empty()

        return False
