import time
import matplotlib.pyplot as plt
from console_progressbar import ProgressBar

from Config import Config
from Consts import FILE, POPULATION_NUMBER, EPOCHS_WITHOUT_BEST, INTERSECTIONS_PENALTY, TOURNAMENT_SIZE, \
    CROSS_PROBABILITY, PATH_MUTATION_PROBABILITY
from Population import Population
from Solution import cross
import numpy as np

from Tools import get_init_intersections_pentalties


class Problem:

    def __init__(self):
        config = Config.initialize(FILE)
        self.config = config

    def run_problem(self, max_epochs, tournament_size, cross_prob, mutate_prob, is_tournament, population_size):
        intersections_pentalties = get_init_intersections_pentalties(len(self.config.pairs))
        result = []
        prev_population = Population(self.config)

        prev_population.get_init_population(population_size)
        best = prev_population.get_best(intersections_pentalties)
        counter = 0
        epoch = 0
        best.get_all_points()
        intersections_pentalties = best.get_next_intersections(intersections_pentalties)
        # result.append([best.fitness, prev_population.get_worst(intersections_pentalties).fitness, prev_population.get_avg(intersections_pentalties)])
        while self.condition(counter, max_epochs):
            epoch += 1
            next_pop = Population(self.config)
            next_pop.get_init_population(population_size)
            while len(next_pop) != population_size:
                parent1 = prev_population.tournament(tournament_size, intersections_pentalties) if is_tournament else prev_population.roulette()
                parent2 = prev_population.tournament(tournament_size, intersections_pentalties) if is_tournament else prev_population.roulette()

                new_solution = cross(parent1, parent2, self.config, cross_prob)
                new_solution.mutate(mutate_prob)
                next_pop.add_solution(new_solution)

            new_best = next_pop.get_best(intersections_pentalties)
            prev_population = next_pop
            # result.append([new_best.fitness, next_pop.get_worst(intersections_pentalties).fitness, next_pop.get_avg(intersections_pentalties)])
            if new_best.get_fitness(intersections_pentalties) < best.get_fitness(intersections_pentalties):
                best = new_best
                # intersections_pentalties = get_init_intersections_pentalties(len(self.config.pairs))

            intersections_pentalties = best.get_next_intersections(intersections_pentalties)

            print("Najlepszy: " + str(best.get_fitness(intersections_pentalties)), "Aktualny: ", str(new_best.get_fitness(intersections_pentalties)), "kary: ", intersections_pentalties)
            counter += 1
        best.to_png(intersections_pentalties)
        return result

    def condition(self, counter, max_epochs):
        return counter < max_epochs


if __name__ == "__main__":

    problem = Problem()
    x = problem.run_problem(30, TOURNAMENT_SIZE, CROSS_PROBABILITY, PATH_MUTATION_PROBABILITY, True, POPULATION_NUMBER)
    # populations = [50, 100, 200, 500, 1000]
    # epochs = [10, 50, 100, 200, 300, 500]
    #
    # mutate_probs = [0.05, 0.1, 0.15, 0.25, 0.4]
    # cross_probs = [0.2, 0.25, 0.3, 0.4, 0.5]
    # tournaments = [0.05, 0.1, 0.2, 0.3, 0.4]
    #
    # temp1 = [[], [], []]
    # temp = [[], [], []]
    #
    # for mutate_prob in mutate_probs:
    #     print(f"Mutacja: {mutate_prob}")
    #     for i in range(0, 10):
    #         x = problem.run_problem(EPOCHS_WITHOUT_BEST, TOURNAMENT_SIZE, CROSS_PROBABILITY, mutate_prob, True, POPULATION_NUMBER)
    #         bests = list(map(lambda _x: _x[0], x))
    #         worsts = list(map(lambda _x: _x[1], x))
    #         avgs = list(map(lambda _x: _x[2], x))
    #         temp[0].append(bests)
    #         temp[1].append(worsts)
    #         temp[2].append(avgs)
    #
    #         temp1[0].extend(bests)
    #         temp1[1].extend(worsts)
    #         temp1[2].extend(avgs)
    #
    #     f = open("assets/different_mutations/mutations.txt", "a")
    #     f.flush()
    #     f.write(f"Mutacja({mutate_prob}): {np.min(temp1[0])}, {np.max(temp1[1])}, {np.mean(temp1[2])}\n")
    #     f.close()
    #     xx = range(0, len(temp[0][0]))
    #     plt.plot(xx, np.mean(temp[0], axis=0), label="Best")
    #     plt.plot(xx, np.mean(temp[1], axis=0), label="Worst")
    #     plt.plot(xx, np.mean(temp[2], axis=0), label="Average")
    #     plt.legend()
    #     plt.title(f"Mutacja: {mutate_prob}")
    #     plt.savefig(f"assets/different_mutations/plots/mutation{str(mutate_prob).replace('.', '')}.png")
    #     plt.cla()
    #     temp = [[], [], []]
    #     temp1 = [[], [], []]
    #
    # plt.cla()
    # temp = [[], [], []]
    # temp1 = [[], [], []]
    #
    # for population in populations:
    #     print(f"Mutacja: {population}")
    #     for i in range(0, 10):
    #         x = problem.run_problem(EPOCHS_WITHOUT_BEST, TOURNAMENT_SIZE, CROSS_PROBABILITY, PATH_MUTATION_PROBABILITY, True, population)
    #         bests = list(map(lambda _x: _x[0], x))
    #         worsts = list(map(lambda _x: _x[1], x))
    #         avgs = list(map(lambda _x: _x[2], x))
    #         temp[0].append(bests)
    #         temp[1].append(worsts)
    #         temp[2].append(avgs)
    #
    #         temp1[0].extend(bests)
    #         temp1[1].extend(worsts)
    #         temp1[2].extend(avgs)
    #
    #     f = open("assets/different_population/populations.txt", "a")
    #     f.flush()
    #     f.write(f"Populacja ({population}): {np.min(temp1[0])}, {np.max(temp1[1])}, {np.mean(temp1[2])}\n")
    #     f.close()
    #     xx = range(0, len(temp[0][0]))
    #     plt.plot(xx, np.mean(temp[0], axis=0), label="Best")
    #     plt.plot(xx, np.mean(temp[1], axis=0), label="Worst")
    #     plt.plot(xx, np.mean(temp[2], axis=0), label="Average")
    #     plt.legend()
    #     plt.title(f"Populacja: {population} osobników")
    #     plt.savefig(f"assets/different_population/plots/population{str(population)}.png")
    #     plt.cla()
    #     temp = [[], [], []]
    #     temp1 = [[], [], []]
    #
    # plt.cla()
    # temp = [[], [], []]
    # temp1 = [[], [], []]
    #
    # for epoch in epochs:
    #     print(f"Epoki: {epoch}")
    #     for i in range(0, 10):
    #         x = problem.run_problem(epoch, TOURNAMENT_SIZE, CROSS_PROBABILITY, PATH_MUTATION_PROBABILITY, True, POPULATION_NUMBER)
    #         bests = list(map(lambda _x: _x[0], x))
    #         worsts = list(map(lambda _x: _x[1], x))
    #         avgs = list(map(lambda _x: _x[2], x))
    #         temp[0].append(bests)
    #         temp[1].append(worsts)
    #         temp[2].append(avgs)
    #
    #         temp1[0].extend(bests)
    #         temp1[1].extend(worsts)
    #         temp1[2].extend(avgs)
    #
    #     f = open("assets/different_epochs/epochs.txt", "a")
    #     f.flush()
    #     f.write(f"Epoka ({epoch}): {np.min(temp1[0])}, {np.max(temp1[1])}, {np.mean(temp1[2])}\n")
    #     f.close()
    #     xx = range(0, len(temp[0][0]))
    #     plt.plot(xx, np.mean(temp[0], axis=0), label="Best")
    #     plt.plot(xx, np.mean(temp[1], axis=0), label="Worst")
    #     plt.plot(xx, np.mean(temp[2], axis=0), label="Average")
    #     plt.legend()
    #     plt.title(f"Epoka: {epoch}")
    #     plt.savefig(f"assets/different_epochs/plots/epoch{str(epoch)}.png")
    #     plt.cla()
    #     temp = [[], [], []]
    #     temp1 = [[], [], []]
    #
    # plt.cla()
    # temp = [[], [], []]
    # temp1 = [[], [], []]
    #
    # for cross_prob in cross_probs:
    #     print(f"Prawd. crossowania: {cross_prob}")
    #     for i in range(0, 10):
    #         x = problem.run_problem(EPOCHS_WITHOUT_BEST, TOURNAMENT_SIZE, cross_prob, PATH_MUTATION_PROBABILITY, True, POPULATION_NUMBER)
    #         bests = list(map(lambda _x: _x[0], x))
    #         worsts = list(map(lambda _x: _x[1], x))
    #         avgs = list(map(lambda _x: _x[2], x))
    #         temp[0].append(bests)
    #         temp[1].append(worsts)
    #         temp[2].append(avgs)
    #
    #         temp1[0].extend(bests)
    #         temp1[1].extend(worsts)
    #         temp1[2].extend(avgs)
    #
    #     f = open("assets/different_cross/cross.txt", "a")
    #     f.flush()
    #     f.write(f"Prawd. crossowania ({cross_prob}): {np.min(temp1[0])}, {np.max(temp1[1])}, {np.mean(temp1[2])}\n")
    #     f.close()
    #     xx = range(0, len(temp[0][0]))
    #     plt.plot(xx, np.mean(temp[0], axis=0), label="Best")
    #     plt.plot(xx, np.mean(temp[1], axis=0), label="Worst")
    #     plt.plot(xx, np.mean(temp[2], axis=0), label="Average")
    #     plt.legend()
    #     plt.title(f"Prawd. crossowania: {cross_prob}")
    #     plt.savefig(f"assets/different_cross/plots/crossprob{str(cross_prob).replace('.', '')}.png")
    #     plt.cla()
    #     temp = [[], [], []]
    #     temp1 = [[], [], []]
    #
    # plt.cla()
    # temp = [[], [], []]
    # temp1 = [[], [], []]
    #
    # for tournament in tournaments:
    #     print(f"Turniej: {tournament}")
    #     for i in range(0, 10):
    #         x = problem.run_problem(EPOCHS_WITHOUT_BEST, int(POPULATION_NUMBER*tournament), CROSS_PROBABILITY, PATH_MUTATION_PROBABILITY,
    #                                 True, POPULATION_NUMBER)
    #         bests = list(map(lambda _x: _x[0], x))
    #         worsts = list(map(lambda _x: _x[1], x))
    #         avgs = list(map(lambda _x: _x[2], x))
    #         temp[0].append(bests)
    #         temp[1].append(worsts)
    #         temp[2].append(avgs)
    #
    #         temp1[0].extend(bests)
    #         temp1[1].extend(worsts)
    #         temp1[2].extend(avgs)
    #
    #     f = open("assets/different_tournaments/tournament.txt", "a")
    #     f.flush()
    #     f.write(f"Turniej ({tournament}): {np.min(temp1[0])}, {np.max(temp1[1])}, {np.mean(temp1[2])}\n")
    #     f.close()
    #     xx = range(0, len(temp[0][0]))
    #     plt.plot(xx, np.mean(temp[0], axis=0), label="Best")
    #     plt.plot(xx, np.mean(temp[1], axis=0), label="Worst")
    #     plt.plot(xx, np.mean(temp[2], axis=0), label="Average")
    #     plt.legend()
    #     plt.title(f"Turniej: {tournament}")
    #     plt.savefig(f"assets/different_tournaments/plots/tournament{str(tournament).replace('.', '')}.png")
    #     plt.cla()
    #     temp = [[], [], []]
    #     temp1 = [[], [], []]
    #
    # for i in range(0, 10):
    #     x = problem.run_problem(EPOCHS_WITHOUT_BEST, TOURNAMENT_SIZE, CROSS_PROBABILITY, PATH_MUTATION_PROBABILITY, False, POPULATION_NUMBER)
    #     bests = list(map(lambda _x: _x[0], x))
    #     worsts = list(map(lambda _x: _x[1], x))
    #     avgs = list(map(lambda _x: _x[2], x))
    #     temp[0].append(bests)
    #     temp[1].append(worsts)
    #     temp[2].append(avgs)
    #
    #     temp1[0].extend(bests)
    #     temp1[1].extend(worsts)
    #     temp1[2].extend(avgs)
    #
    # f = open("assets/roulette/ruletka.txt", "a")
    # f.flush()
    # f.write(f"Ruletka: {np.min(temp1[0])}, {np.max(temp1[1])}, {np.mean(temp1[2])}\n")
    # f.close()
    # xx = range(0, len(temp[0][0]))
    # plt.plot(xx, np.mean(temp[0], axis=0), label="Best")
    # plt.plot(xx, np.mean(temp[1], axis=0), label="Worst")
    # plt.plot(xx, np.mean(temp[2], axis=0), label="Average")
    # plt.legend()
    # plt.title(f"Ruletka")
    # plt.savefig(f"assets/roulette/plots/ruletka.png")
    # plt.cla()
    # temp = [[], [], []]
    # temp1 = [[], [], []]