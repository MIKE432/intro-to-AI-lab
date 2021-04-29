from implementations.BotPlayer import BotPlayer
from implementations.Consts import PLAYER_TWO, PLAYER_ONE
from implementations.Mancala import Mancala, AIvsAI
from implementations.NormalPlayer import NormalPlayer

if __name__ == "__main__":
    p1 = NormalPlayer(PLAYER_ONE)
    p2 = BotPlayer(PLAYER_TWO, 7)
    game = Mancala(p1, p2)
    game.run()
    # AIvsAI(game)
