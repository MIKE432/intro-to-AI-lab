from Consts import FIRST_SPLITTER, SECOND_SPLITTER, TOP, RIGHT, BOTTOM, LEFT
from Exceptions import NoPointsToConnectException, WrongEntryFileFormat


def process_file(lines):
    lines_len = len(lines)

    if lines_len < 2:
        raise NoPointsToConnectException()

    width, height = process_dim_line(lines[0])
    points = []

    for i in range(1, lines_len):
        processed_line = process_points_line(lines[i])
        points.append(processed_line)

    return width, height, points


def process_dim_line(line: str):
    dims = line.split(FIRST_SPLITTER)
    dims_len = len(dims)
    if dims_len != 2:
        raise WrongEntryFileFormat("Wrong number of dimensions. Expected 2 got: " + str(dims_len))

    return int(dims[0]), int(dims[1])


def process_points_line(line: str):
    points = line.split(FIRST_SPLITTER)
    if len(points) != 2:
        raise WrongEntryFileFormat("Wrong number of points in line. Expected 2 got: " + str(len(points)))

    start = get_point_coordinates(points[0])
    end = get_point_coordinates(points[1])

    return start, end


def get_point_coordinates(point: str):
    coordinates = point.split(SECOND_SPLITTER)

    if len(coordinates) != 2:
        raise WrongEntryFileFormat("Wrong number of points coordinates. Expected 2 got: " + str(len(coordinates)))

    return int(coordinates[0]), int(coordinates[1])


def get_current_position(prev_position, direction, length):
    if direction == TOP:
        return [prev_position[0], prev_position[1] + length]
    elif direction == RIGHT:
        return [prev_position[0] + length, prev_position[1]]
    elif direction == BOTTOM:
        return [prev_position[0], prev_position[1] - length]
    elif direction == LEFT:
        return [prev_position[0] - length, prev_position[1]]


def is_in_board(point, width, height):
    return 0 <= point[0] <= width and 0 <= point[1] <= height
