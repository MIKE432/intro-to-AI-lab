from random import randint

import numpy as np

from Config import Config
from Consts import MUTATE_MOVE
from SolutionTools import get_random_vector, get_length_to_edge
from Tools import get_current_position, is_in_board


class Path:
    def __init__(self, start, end, config: Config, segments=None):
        self.start = start
        self.end = end
        if segments is None:
            self.segments = []
        else:
            self.segments = segments
        self.configuration = config

    def randomize(self):
        current_position = [self.start[0], self.start[1]]
        prev_dir = -1
        while current_position != [self.end[0], self.end[1]]:
            res = get_random_vector(current_position, self.end, prev_dir, self.configuration.width,
                                    self.configuration.height)
            self.segments.append(res)
            current_position = get_current_position(current_position, res[0], res[1])

            prev_dir = res[0]

    def __getitem__(self, item):
        return self.segments[item]

    def __len__(self):
        return len(self.segments)

    def out_of_board_length(self):
        length = 0
        number = 0
        curr = self.start
        for direction, l in self.segments:
            end = get_current_position(curr, direction, l)
            end_in_board = is_in_board(end, self.configuration.width, self.configuration.height)
            start_in_board = is_in_board(curr, self.configuration.width, self.configuration.height)

            if not start_in_board and not end_in_board:
                length += l
                number += 1
            elif not start_in_board and end_in_board:
                length = l - get_length_to_edge(end, (direction + 2) % 4, self.configuration.width,
                                                self.configuration.height)
                number += 1
            elif start_in_board and not end_in_board:
                length = l - get_length_to_edge(end, direction, self.configuration.width,
                                                self.configuration.height)
                number += 1
            curr = end

    def get_points(self):
        points = [self.start]
        curr = points[0]
        for direction, l in self.segments:
            curr = get_current_position(curr, direction, l)
            points.append(curr)

        return points

    def mutate(self):
        self.__mutation_type_a()

    def __mutation_type_a(self):
        random_direction_prob = np.random.random(1)[0]
        random_segment_index = randint(0, len(self.segments) - 1)
        curr_direction, curr_l = self.segments[random_segment_index]
        direction = -1
        prev_segment_to_insert = None
        next_segment_to_insert = None

        if curr_direction in [0, 2]:
            direction = 1 if random_direction_prob > 0.5 else 3
        else:
            direction = 2 if random_direction_prob > 0.5 else 0

        # prev
        if random_segment_index > 0:
            prev_direction, prev_l = self.segments[random_segment_index - 1]
            if prev_direction == curr_direction:
                prev_segment_to_insert = [direction, MUTATE_MOVE]
            else:
                self.segments[random_segment_index - 1][1] += 1 if direction == prev_direction else -1
                if self.segments[random_segment_index - 1][1] == 0:
                    self.segments.remove(random_segment_index - 1)
        else:
            prev_segment_to_insert = [direction, MUTATE_MOVE]

        # next
        if random_segment_index != len(self.segments) - 1:
            next_direction, next_l = self.segments[random_segment_index + 1]
            if next_direction == curr_direction:
                next_segment_to_insert = [(direction + 2) % 4, MUTATE_MOVE]
            else:
                self.segments[random_segment_index + 1][1] += 1 if direction != next_direction else -1
                if self.segments[random_segment_index + 1][1] == 0:
                    self.segments.remove(random_segment_index + 1)
        else:
            next_segment_to_insert = [(direction + 2) % 4, MUTATE_MOVE]

        if next_segment_to_insert is not None:
            self.segments.insert(random_segment_index + 1, next_segment_to_insert)

        if prev_segment_to_insert is not None:
            self.segments.insert(random_segment_index, prev_segment_to_insert)
            # insert poprzedni na i a następny na i + 1

        test = self.is_correct()

    def is_correct(self):
        curr = self.start
        for direction, l in self.segments:
            curr = get_current_position(curr, direction, l)
        x = curr == self.end
        return x
