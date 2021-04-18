from abstracts.Player import Player
from implementations.BotPlayer import BotPlayer
from implementations.Consts import PLAYER_TWO, PLAYER_ONE
from implementations.Mancala import Mancala
from implementations.MancalaDecisionTree import apply_decision_tree_to_root, MancalaDecisionNode
from implementations.NormalPlayer import NormalPlayer

if __name__ == "__main__":
    p1 = BotPlayer(PLAYER_ONE, 5)
    p2 = NormalPlayer(PLAYER_TWO)
    game = Mancala(p1, p2)
    game.run()