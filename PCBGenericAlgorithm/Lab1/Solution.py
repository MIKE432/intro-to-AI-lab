import json
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

    def get_fitness(self):
        return self.__calculate_fitness

    @classmethod
    def from_random(cls, configuration: Config):
        ind = Solution(configuration)
        ind.randomize()
        return ind

    @classmethod
    def from_best_random(cls, configuration: Config, iteration: int):
        best = Solution(configuration)
        best.randomize()

        for i in range(0, iteration - 1):
            candidate = Solution(configuration)
            candidate.randomize()
            if candidate < best:
                best = candidate

        return best

    @property
    def fitness(self):
        return self.__get_fitness_by_lazy()

    def __get_fitness_by_lazy(self):
        if self.__fitness is None:
            self.__fitness = self.__calculate_fitness

        return self.__fitness

    @property
    def __calculate_fitness(self):
        all_segments = []

        for segment in self.paths:
            all_segments.extend(segment)

        length_sum = sum(map(lambda _x: _x[1], all_segments))
        if len(all_segments) == 4:
            x = 10
        out_of_board_sum, out_of_board = self.__get_out_of_board_length()
        intersections = self.__get_intersection_number()
        return \
            length_sum + len(all_segments) \
            + (out_of_board_sum * SUM_OUT_OF_BOARD_PENALTY) \
            + (out_of_board * OUT_OF_BOARD_PENALTY) \
            + (intersections * INTERSECTIONS_PENALTY)

    def __get_intersection_number(self):
        intersections = 0
        points = self.configuration.pairs

        segments = []

        for i in range(0, len(self.paths)):
            start = points[i]
            curr = []
            for j in range(0, len(self.paths[i])):
                curr.append(get_n_segment(start, self.paths[i], j))
            segments.append(curr)

        for i in range(0, len(segments)):
            for j in range(0, len(segments[i])):
                for k in range(0, len(segments)):
                    for l in range(j + 2 if i == k else 0, len(segments[k])):
                        if are_segments_intersecting(segments[i][j], segments[k][l]):
                            intersections += 1

        return intersections

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

    # def to_matrix(self):
    #     width = self.configuration.width * 10
    #     height = self.configuration.height * 10
    #     matrix = np.zeros(width, height)
    #     start_point = int(width/2) + self.configuration.width, int(height/2) + self.configuration.height
    #     for i in range(0, len(self.paths)):
    #         start = self.configuration.pairs[i][0]
    #         curr = start[0] + start_point[0], start[1] + start_point[0]
    #         for direction, l in self.paths[i]:
    #
    #             if direction == TOP:
    #
    #
    #             curr = get_current_position(curr, direction, l)
    #
    #     return matrix

    def to_json(self):
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
        json = SolutionJSON(paths, points, width, height, self.fitness, generation)
        return json.to_json()

    def to_json_file(self):
        _json = self.to_json()
        f = open(JSON_FILE, "w")
        f.write(_json)
        f.close()

    def to_png(self):
        self.to_json_file()
        store_png()

    def mutate(self):
        for path in self.paths:
            random = np.random.random(1)[0]
            if random <= PATH_MUTATION_PROBABILITY:
                path.mutate()

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __le__(self, other):
        return not self >= other

    def __eq__(self, other):
        return other.fitness == self.fitness

    def __ne__(self, other):
        return not other == self

    def __str__(self):
        pass


def cross(parent1: Solution, parent2: Solution, configuration: Config):
    paths = []
    random = np.random.random(1)[0]

    if random <= CROSS_PROBABILITY:
        point = randint(0, len(parent1.paths))
        paths.extend(parent1.paths[:point])
        paths.extend(parent2.paths[point:])
    else:
        if random > .5:
            paths.extend(parent1.paths)
        else:
            paths.extend(parent2.paths)

    return Solution(configuration, paths)
