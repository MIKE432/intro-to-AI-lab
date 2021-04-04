from Tools import remove_from_domain
from abstracts.Problem import Problem
from abstracts.Variable import Variable


def forward_checking(problem: Problem, current: Variable, removed):
    counter = 0
    for neighbour in current.neighbours:
        if not neighbour.is_value_changed():
            for value in neighbour.domain:
                neighbour.value = value
                if not problem.constraint(current, neighbour):
                    remove_from_domain(neighbour, value, removed)
                else:
                    counter += 1

            neighbour.to_empty()
            if counter == 0:
                return False
    return True
