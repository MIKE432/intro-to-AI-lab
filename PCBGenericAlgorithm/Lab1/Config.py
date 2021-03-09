from Tools import process_file


class Config:
    """
        @:param pcb_width width of the pcb board > 0
        @:param pcb_height height of the pcb board > 0
        @:param pair_of_points list of pairs of coordinates of the points to connect
    """

    def __init__(self, pcb_width, pcb_height, pairs_of_points):
        self.height = pcb_height
        self.width = pcb_width
        self.pairs = pairs_of_points

    @classmethod
    def initialize(cls, file_path):
        f = open(file_path, "r")
        width, height, list_of_pairs = process_file(f.readlines())
        return Config(width, height, list_of_pairs)
