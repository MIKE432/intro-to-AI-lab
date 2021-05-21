from abstracts.Player import Player


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self.current_player = None
        self.pick_first_player()

    def pick_first_player(self):
        self.current_player = self.players[0]

    def end_condition(self):
        return True

    def run(self, disable_print=False):
        while not self.end_condition():
            self.turn_procedure()
            self.switch_players()
            if not disable_print:
                print(self)
        print(self.sum_points())

    def switch_players(self):
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

    def sum_points(self):
        pass

    def turn_procedure(self):
        pass
