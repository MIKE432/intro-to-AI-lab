from numpy import mean

from Config import Config
from Consts import BEST_INIT_ITERATION
from Solution import Solution
from console_progressbar import ProgressBar


class Population:

    def __init__(self, config: Config):
        self.config = config
        self.population = []

    def get_init_population(self, x):
        pb = ProgressBar(total=1000, prefix='Population initialization', suffix='Completed', decimals=1, length=50,
                         fill='X', zfill='-')
        curr = []
        for progress in range(x):
            curr.append(Solution.from_best_random(self.config, BEST_INIT_ITERATION))
            pb.print_progress_bar(progress)
        self.population = curr

    def get_mean(self):
        ints = list(map(lambda _x: _x.fitness, self.population))
        x = min(self.population, key=lambda _x: _x.fitness)
        x.get_fitness()
        return x
