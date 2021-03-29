import json
from copy import deepcopy
from random import randint

import numpy as np

from Config import Config
from Consts import SUM_OUT_OF_BOARD_PENALTY, OUT_OF_BOARD_PENALTY, INTERSECTIONS_PENALTY, JSON_FILE, CROSS_PROBABILITY, \
    INHERIT_PARENT, PATH_MUTATION_PROBABILITY
from Path import Path
from SolutionTools import get_length_to_edge, are_segments_intersecting, get_n_segment
from Tools import get_current_position, is_in_board
import UI
from printer.generator import store_png


class SolutionJSON:
    def __init__(self, paths, points, width, height, fitness, generation=1):
        self.board = [width, height]
        self.paths = paths
        self.points = points
        self.fitness = fitness
        self.generation = generation

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Solution:

    def __init__(self, configuration: Config, paths=None):
        if paths is not None:
            self.paths = paths
        else:
            self.paths = []
        self.__fitness = None
        self.configuration = configuration

    def randomize(self):
        for start, end in self.configuration.pairs:
            current_path = Path(start, end, self.configuration)
            current_path.randomize()
            self.paths.append(current_path)

    def get_fitness(self, intersections):
        return self.__calculate_fitness(intersections)

    @classmethod
    def from_random(cls, configuration: Config):
        ind = Solution(configuration)
        ind.randomize()
        return ind

    @classmethod
    def from_best_random(cls, configuration: Config, iteration: int, intersections):
        best = Solution(configuration)
        best.randomize()

        for i in range(0, iteration - 1):
            candidate = Solution(configuration)
            candidate.randomize()
            if candidate.fitness(intersections) < best.fitness(intersections):
                best = candidate

        return best

    def get_next_intersections(self, prev_intersections):
        _x = {}

        for i in prev_intersections.keys():
            for j in prev_intersections[i].keys():
                if self.paths[i].intersects_with(self.paths[j]) > 0:
                    prev_intersections[i][j] += INTERSECTIONS_PENALTY

        return prev_intersections

    def fitness(self, intersections):
        return self.__get_fitness_by_lazy(intersections)

    def __get_fitness_by_lazy(self, intersections):
        if self.__fitness is None:
            self.__fitness = self.__calculate_fitness(intersections)

        return self.__fitness

    def __calculate_fitness(self, intersections):
        all_segments = []

        for segment in self.paths:
            all_segments.extend(segment)

        length_sum = sum(map(lambda _x: _x[1], all_segments))
        out_of_board_sum, out_of_board = self.__get_out_of_board_length()
        intersections_penalty = self.__get_intersection_penalty(intersections)

        return \
            length_sum \
            + (out_of_board_sum * SUM_OUT_OF_BOARD_PENALTY) \
            + (out_of_board * OUT_OF_BOARD_PENALTY) \
            + intersections_penalty

    def __get_intersection_penalty(self, intersections):
        penalty = 0

        for i in range(0, len(self.paths)):
            for j in range(0, len(self.paths)):
                if i != j:
                    if self.paths[i].intersects_with(self.paths[j]):
                        penalty += intersections[i][j]

        return penalty

    def get_all_points(self):
        points = []
        for path in self.paths:
            points.extend(path.get_every_points())

        return points

    def __get_out_of_board_length(self):
        points = self.configuration.pairs
        length = 0
        number = 0
        for i in range(0, len(points)):
            curr = points[i][0]
            for direction, l in self.paths[i]:
                end = get_current_position(curr, direction, l)
                end_in_board = is_in_board(end, self.configuration.width, self.configuration.height)
                start_in_board = is_in_board(curr, self.configuration.width, self.configuration.height)

                if not start_in_board and not end_in_board:
                    length += l
                    number += 1
                elif not start_in_board and end_in_board:
                    length = get_length_to_edge(end, (direction + 2) % 4, self.configuration.width,
                                                self.configuration.height)
                    number += 1
                elif start_in_board and not end_in_board:
                    length = get_length_to_edge(end, direction, self.configuration.width,
                                                self.configuration.height)
                    number += 1
                curr = end

        return length, number

    def to_json(self, intersections):
        width = self.configuration.width
        height = self.configuration.height
        generation = 1
        paths = []
        points = []

        for path in self.paths:
            paths.append(path.get_points())

        for _points in self.configuration.pairs:
            points.append(_points[0])
            points.append(_points[1])
        json = SolutionJSON(paths, points, width, height, self.fitness(intersections), generation)
        return json.to_json()

    def to_json_file(self, intersections):
        _json = self.to_json(intersections)
        f = open(JSON_FILE, "w")
        f.write(_json)
        f.close()

    def to_png(self, intersections):
        self.to_json_file(intersections)
        store_png()

    def mutate(self, mutate_prob):
        for path in self.paths:
            random = np.random.random(1)[0]
            if random <= mutate_prob:
                path.mutate()


def cross(parent1: Solution, parent2: Solution, configuration: Config, cross_prob):
    paths = []
    random = np.random.random(1)[0]

    if random <= cross_prob:
        point = randint(0, len(parent1.paths))
        paths.extend(deepcopy(parent1.paths[:point]))
        paths.extend(deepcopy(parent2.paths[point:]))
    else:
        if random > .5:
            paths.extend(deepcopy(parent1.paths))
        else:
            paths.extend(deepcopy(parent2.paths))

    return Solution(configuration, deepcopy(paths))
