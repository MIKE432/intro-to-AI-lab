def no_checking(problem, current, removed):
    return True


def no_constraint(node1, node2):
    return True


def no_sort(problem, node):
    return node.domain


def overridden_next(problem):
    return problem.next()
