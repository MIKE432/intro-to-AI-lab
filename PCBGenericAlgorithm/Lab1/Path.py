from Config import Config
from Solution import get_random_vector
from Tools import get_current_position


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