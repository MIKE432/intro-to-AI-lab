import time

from Config import Config
from Consts import FILE, POPULATION_NUMBER, EPOCHS_WITHOUT_BEST
from Population import Population
from Solution import cross


class Problem:

    def __init__(self):
        config = Config.initialize(FILE)
        self.config = config

    def run_problem(self):
        prev_population = Population(self.config)
        prev_population.get_init_population(POPULATION_NUMBER)
        best = prev_population.get_best()
        counter = 0
        epoch = 0

        print("\n")

        while counter > EPOCHS_WITHOUT_BEST:
            epoch += 1
            next_pop = Population(self.config)
            while len(next_pop) == POPULATION_NUMBER:
                parent1 = prev_population.tournament()
                parent2 = prev_population.roulette()

                new_solution = cross(parent1, parent2, self.config)
                new_solution.mutate()

                if new_solution > best:
                    best = new_solution
                    counter = 0

        best.to_png()



if __name__ == "__main__":
    x = 1 / 7 + 1 / 2 + 1 / 5

    a = 1 / (2 * x)
    b = 1 / (7 * x)
    c = 1 / (5 * x)
    xx = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    xx.insert(8 + 1, 10)
    print(xx)
    problem = Problem()
    problem.run_problem()
