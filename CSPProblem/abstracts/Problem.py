from typing import List

from abstracts.Variable import Variable


class Problem:
    # constraints are functions that applies to specific/all nodes by passing node/all nodes as a parameter
    def __init__(self, domain):
        self.nodes = []
        self.domain = domain
        self.constraints = []
        self.nodes_constraints = {}

    def apply_nodes(self, nodes: List):
        self.nodes = nodes

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def add_node_specific_constraint(self, nodeNum, constraint):
        if nodeNum > len(self.nodes):
            raise IndexError(f"there is no such node with index: {nodeNum}, number of nodes: {len(self.nodes)}")

        if nodeNum not in self.nodes_constraints:
            self.nodes_constraints[nodeNum] = [constraint]
        else:
            self.nodes_constraints[nodeNum].append(constraint)

    def are_constraints_satisfied(self):
        for constraint in self.constraints:
            if not constraint(self.nodes):
                return False

        for key in self.nodes_constraints.keys():
            node = self.nodes[key]
            constraints = self.nodes_constraints[key]
            for constraint in constraints:
                if not constraint(node):
                    return False
        return True

    def next(self):
        pass

    def add_node(self, node: Variable):
        self.nodes.append(node)
