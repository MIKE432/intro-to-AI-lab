from abstracts.Problem import Problem
from abstracts.Resolver import Resolver


class BackTracking(Resolver):
    def __init__(self, problem: Problem):
        super().__init__(problem)
        self.solutions = []

    def resolve_problem(self):
        return self.backtrack()

    def accept(self):
        return self.problem.are_constraints_satisfied()

    def backtrack(self):
        next_empty = self.problem.next()
        if next_empty is None:
            return True

        for val in next_empty.domain:
            next_empty.pick_random_value(val)
            if self.accept():
                if self.backtrack():
                    return True

            next_empty.to_empty()

        return False
