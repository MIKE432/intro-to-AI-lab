from Config import Config
from Solution import get_random_vector, get_length_to_edge
from Tools import get_current_position, is_in_board


class Path:
    def __init__(self, start, end, config: Config, segments=None):
        self.start = start
        self.end = end
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
                length = get_length_to_edge(end, (direction + 2) % 4, self.configuration.width,
                                            self.configuration.height)
                number += 1
            elif start_in_board and not end_in_board:
                length = get_length_to_edge(end, direction, self.configuration.width,
                                            self.configuration.height)
                number += 1
            curr = end
