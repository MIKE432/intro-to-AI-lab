from copy import deepcopy
from random import randint
from typing import List


class Variable:
    def __init__(self, def_val, domain: List):
        self.value = deepcopy(def_val)
        self._domain = sorted(deepcopy(domain))
        self._def_domain = deepcopy(domain)
        self.def_val = def_val
        self.neighbours = []

    def pick_random_value(self, predefined=None):
        if predefined is not None:
            self.value = predefined
            return
        self.value = randint(0, len(self.domain))

    @property
    def domain(self):
        return self._domain

    def set_domain(self, domain: list):
        self._domain = domain

    def is_value_changed(self):
        return self.def_val != self.value

    def to_empty(self):
        self.value = self.def_val

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def add_to_domain(self, item):
        self.domain.append(item)
        self._domain = sorted(self._domain)

    def __str__(self):
        return str(self.value) + " " + str(self.domain)

    def reset(self):
        self.to_empty()
        self._domain = deepcopy(self._def_domain)
