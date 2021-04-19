from UI import init
from abstracts.Player import Player
from implementations.BotPlayer import BotPlayer
from implementations.Consts import PLAYER_TWO, PLAYER_ONE
from implementations.Mancala import Mancala, AIvsAI
from implementations.MancalaDecisionTree import apply_decision_tree_to_root, MancalaDecisionNode
from implementations.NormalPlayer import NormalPlayer

if __name__ == "__main__":
    p1 = BotPlayer(PLAYER_ONE, 3)
    p2 = BotPlayer(PLAYER_TWO, 5)
    game = Mancala(p1, p2)
    # init(game)
    AIvsAI(game)
