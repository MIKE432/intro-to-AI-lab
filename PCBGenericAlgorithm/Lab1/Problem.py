from Config import Config
from Population import Population

FILE = "test_file2"


class Problem:

    def __init__(self):
        config = Config.initialize(FILE)
        self.config = config
        self.population = Population(config)

    def run_problem(self):
        self.population.get_init_population(1000)
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
    problem = Problem()
    problem.run_problem()
