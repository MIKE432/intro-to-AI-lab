import time

from implementations.BotPlayer import BotPlayer
from implementations.Consts import PLAYER_TWO, PLAYER_ONE
from implementations.Mancala import Mancala, AIvsAI
from implementations.NormalPlayer import NormalPlayer
from report import report

if __name__ == "__main__":
    # p1 = BotPlayer(PLAYER_ONE, 6, use_alpha_beta=False)
    # p2 = BotPlayer(PLAYER_TWO, 6, use_alpha_beta=False)
    # game = Mancala(p1, p2)
    # # game.run()
    # start = time.time()
    # AIvsAI(game)
    # stop = time.time()
    # print(stop - start)

    alfa, no_alfa = report([2, 3, 4, 5, 6], 1)

    for i in range(0, 2):
        print(f"\nDla poziomu trudności {i} z wykorzystaniem alfy i bety:")
        print(f"Średni czas: {alfa[i][0]}")
        print(f"Średnia ilość ruchów: {alfa[i][1]}")
        print(f"\nDla poziomu trudności {i} bez wykorzystania alfy i bety:")
        print(f"Średni czas: {no_alfa[i][0]}")
        print(f"Średnia ilość ruchów: {no_alfa[i][1]}")
