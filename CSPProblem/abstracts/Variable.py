from copy import deepcopy
from typing import List


class Variable:
    def __init__(self, def_val, domain: List):
        self.value = deepcopy(def_val)
        self.domain = domain
        self.def_val = def_val

    def pick_random_value(self, predefined=None):
        pass

    def set_domain(self, domain: list):
        self.domain = domain

    def are_node_constraints_satisfied(self):
        pass

    def is_value_changed(self):
        return self.def_val != self.value

    def to_empty(self):
        self.value = self.def_val
