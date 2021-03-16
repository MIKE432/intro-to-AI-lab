from random import randint

from shapely.geometry import LineString

from Consts import LEFT, TOP, RIGHT, BOTTOM, CLOSER_PROBABILITY
from Tools import get_current_position


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


def are_segments_intersecting(seg1, seg2):
    l1 = LineString(seg1)
    l2 = LineString(seg2)

    return l1.intersects(l2)


def get_n_segment(start, segments, n):
    curr = start[0]
    i = 0
    for direction, l in segments:
        end = get_current_position(curr, direction, l)
        if i == n:
            return curr, end
        curr = end
        i += 1

    raise IndexError()