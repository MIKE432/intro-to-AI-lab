from typing import List

from abstracts.Player import Player


class NormalPlayer(Player):
    def __init__(self, number):
        super().__init__(number)

    def move(self, choices: List, board, random_move=False):
        return int(input(f"Pick one of given values {choices}: "))
