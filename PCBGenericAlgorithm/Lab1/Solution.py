from random import randint

from Config import Config
from Consts import CLOSER_PROBABILITY, BOTTOM, LEFT, TOP, RIGHT, SUM_OUT_OF_BOARD_PENALTY, OUT_OF_BOARD_PENALTY
from Tools import get_current_position, is_in_board


class Solution:

    def __init__(self, configuration: Config):
        self.segments = []
        self.__fitness = None
        self.configuration = configuration

    def randomize(self, ):
        for start, end in self.configuration.pairs:
            current_position = [start[0], start[1]]
            prev_dir = -1
            current_path = []
            while current_position != [end[0], end[1]]:
                res = get_random_vector(current_position, end, prev_dir, self.configuration.width,
                                        self.configuration.height)
                current_path.append(res)
                current_position = get_current_position(current_position, res[0], res[1])

                prev_dir = res[0]

            self.segments.append(current_path)

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
            self.__fitness = self.__calculate_fitness()

        return self.__fitness

    def __calculate_fitness(self):
        all_segments = []

        for segment in self.segments:
            all_segments.extend(segment)

        length_sum = sum(map(lambda _x: _x[1], all_segments))
        out_of_board_sum, out_of_board = self.__get_out_of_board_length()

        return \
            length_sum + len(all_segments) \
            + (out_of_board_sum * SUM_OUT_OF_BOARD_PENALTY) \
            + (out_of_board * OUT_OF_BOARD_PENALTY)

    def __get_out_of_board_length(self):
        points = self.configuration.pairs
        length = 0
        number = 0
        for i in range(0, len(points)):
            curr = points[i][0]
            for direction, l in self.segments[i]:
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

        return length, number

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


def get_random_vector(curr, end, prev_dir, max_width, max_height):
    dp = determine_directions_probability(curr, end, prev_dir)
    direction = get_random_direction(dp[0], dp[1], dp[2], dp[3])

    isVertical = direction in [0, 2]
    max_len = abs(end[1] - curr[1]) if isVertical else abs(end[0] - curr[0])
    if max_len < 1:
        return [direction, 1]

    length = randint(1, max_len)
    return [direction, length]


def determine_directions_probability(curr, end, prev_direction):
    top = 1
    right = 1
    bottom = 1
    left = 1
    is_prev_vertical = is_vertical(prev_direction)

    if end[0] - curr[0] > 0:
        right = CLOSER_PROBABILITY
    else:
        left = CLOSER_PROBABILITY

    if end[1] - curr[1] > 0:
        top = CLOSER_PROBABILITY
    else:
        bottom = CLOSER_PROBABILITY

    if prev_direction == -1:
        return top, right, bottom, left

    if is_prev_vertical:
        if prev_direction == BOTTOM:
            top = 0
        else:
            bottom = 0
    else:
        if prev_direction == LEFT:
            right = 0
        else:
            left = 0

    return top, right, bottom, left


def is_between(x, a, b):
    return a <= x <= b


def is_vertical(direction):
    return direction in [TOP, BOTTOM]


def get_random_direction(top_prop=1, right_prop=1, bottom_prop=1, left_prop=1):
    top = [0, top_prop * randint(0, 100)]
    right = [1, right_prop * randint(0, 100)]
    bottom = [2, bottom_prop * randint(0, 100)]
    left = [3, left_prop * randint(0, 100)]

    return max([top, right, bottom, left], key=lambda _x: _x[1])[0]


def get_length_to_edge(start, direction, width, height):
    length = None
    if direction == TOP:
        length = height - start[1]
    elif direction == RIGHT:
        length = width - start[0]
    elif direction == BOTTOM:
        length = start[1]
    elif direction == LEFT:
        length = start[0]

    return abs(length)


def is_segment_vertical(segment):
    p1, p2 = segment
    return p1[0] == p2[0]


# def are_segment_intersecting(seg1, seg2):
#     if is_segment_vertical(seg1):
#         if is_segment_vertical(seg2):
#             return seg1[0][0] == seg2[0][0]
#         else:

