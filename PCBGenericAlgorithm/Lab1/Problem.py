import time

from Config import Config
from Consts import FILE, POPULATION_NUMBER
from Population import Population


class Problem:

    def __init__(self):
        config = Config.initialize(FILE)
        self.config = config
        self.population = Population(config)

    def run_problem(self):
        # POPULATION_NUMBER
        self.population.get_init_population(POPULATION_NUMBER)
        x = self.population.roulette()
        self.population.test()
        print(self.population.get_mean())
        if self.population.population[0] > self.population.population[1]:
            x = 10
        if self.population.population[0] < self.population.population[1]:
            x = 10
        if self.population.population[0] >= self.population.population[1]:
            x = 10
        if self.population.population[0] <= self.population.population[1]:
            x = 10

        if self.population.population[0] == self.population.population[1]:
            x = 10
        if self.population.population[0] != self.population.population[1]:
            x = 10


if __name__ == "__main__":
    x = 1 / 7 + 1 / 2 + 1 / 5

    a = 1 / (2 * x)
    b = 1 / (7 * x)
    c = 1 / (5 * x)
    xx = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print(xx[0:1])
    problem = Problem()
    problem.run_problem()
