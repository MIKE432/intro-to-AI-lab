from numpy import mean

from Config import Config
from Consts import BEST_INIT_ITERATION
from Solution import Solution


class Population:

    def __init__(self, config: Config):
        self.config = config
        self.population = []

    def get_init_population(self, x):
        self.population = [Solution.from_best_random(self.config, BEST_INIT_ITERATION) for _ in range(0, x)]

    def get_mean(self):
        ints = list(map(lambda _x: _x.fitness, self.population))
        return mean(ints)
