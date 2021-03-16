import time

from console_progressbar import ProgressBar

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

        while self.condition(counter):
            epoch += 1
            next_pop = Population(self.config)
            pb = ProgressBar(total=POPULATION_NUMBER, prefix=f'Epoch: {epoch}', suffix='Completed', decimals=1,
                             length=50,
                             fill='█', zfill='-')
            while len(next_pop) != POPULATION_NUMBER:
                w = len(next_pop)
                pb.print_progress_bar(w + 1)
                parent1 = prev_population.tournament()
                parent2 = prev_population.roulette()

                new_solution = cross(parent1, parent2, self.config)
                new_solution.mutate()
                next_pop.add_solution(new_solution)

            new_best = next_pop.get_best()
            prev_population = next_pop
            counter += 1
            print("Best: " + str(new_best.fitness) + ", current best: " + str(
                best.fitness) + ", " + "Algorithm ends in: " + str(EPOCHS_WITHOUT_BEST - counter))
            if new_best < best:
                best = new_best
                counter = 0

        best.to_png()

    def condition(self, counter):
        return counter < EPOCHS_WITHOUT_BEST


if __name__ == "__main__":
    problem = Problem()
    problem.run_problem()
