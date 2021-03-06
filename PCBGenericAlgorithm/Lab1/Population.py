from random import randint

import numpy as np

from Config import Config
from Consts import BEST_INIT_ITERATION, TOURNAMENT_SIZE, POPULATION_NUMBER
from Solution import Solution
from console_progressbar import ProgressBar


class Population:

    def __init__(self, config: Config):
        self.config = config
        self.population = []

    def get_init_population(self, x):
        pb = ProgressBar(total=x, prefix='Population initialization', suffix='Completed', decimals=1, length=50,
                         fill='█', zfill='-')
        curr = []
        for progress in range(x):
            curr.append(Solution.from_random(self.config))
            pb.print_progress_bar(progress + 1)
        self.population = curr

    def get_mean(self):
        ints = list(map(lambda _x: _x.fitness, self.population))
        x = min(self.population, key=lambda _x: _x.fitness)
        x.mutate()
        x.to_png()
        return x

    def tournament(self, tournament_size, intersections):
        picked_parents = []

        for i in range(0, tournament_size):
            random = randint(0, len(self.population) - 1)
            while random in picked_parents:
                random = randint(0, len(self.population) - 1)

            picked_parents.append(random)

        potential_winners = list(map(lambda _x: self.population[_x], picked_parents))
        return min(potential_winners, key=lambda _x: _x.get_fitness(intersections))

    def roulette(self):
        weights = []
        for solution in self.population:
            weights.append(1 / solution.fitness)

        weights_sum = np.sum(weights)

        probabilities = list(map(lambda _x: _x / weights_sum, weights))
        random = np.random.random(1)[0]

        for i in range(0, len(probabilities)):
            previous = np.sum(probabilities[0:i + 1])
            if i + 1 == len(probabilities):
                return self.population[i]

            if previous <= random < previous + probabilities[i + 1]:
                return self.population[i]

        return None

    def add_solution(self, solution: Solution):
        self.population.append(solution)

    def __len__(self):
        return len(self.population)

    def get_best(self, intersections):
        return min(self.population, key=lambda _x: _x.get_fitness(intersections))

    def get_worst(self, intersections):
        return max(self.population, key=lambda _x: _x.get_fitness(intersections))

    def get_avg(self, intersections):
        return np.mean([_x.get_fitness(intersections) for _x in self.population])
