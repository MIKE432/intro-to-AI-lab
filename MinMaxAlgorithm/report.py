import time
from statistics import mean

from Tools import create_plot
from implementations.BotPlayer import BotPlayer
from implementations.Mancala import Mancala, AIvsAI
from implementations.Consts import PLAYER_ONE, PLAYER_TWO


def report(a_difficuties, iter=10):
    aa = []
    bb = []

    for a_diff in a_difficuties:
        a = 0
        b = 0
        for i in range(0, iter):
            for j in range(0, 6):
                print(a_diff, "-", i)
                p1 = BotPlayer(PLAYER_ONE, a_diff, first_move=j)
                p2 = BotPlayer(PLAYER_TWO, a_diff, first_move=j)
                game = Mancala(p1, p2)
                AIvsAI(game, True)
                p1_points, p2_points = game.sum_points()
                if p1_points > p2_points:
                    a += 1
                elif p1_points < p2_points:
                    b += 1
                else:
                    a += 1
                    b += 1
        aa.append(a)
        bb.append(b)
    print(aa, bb)
    t = []
    m = []

    # ab_moves = {}
    # ab_time = {}
    #
    # for a_diff in a_difficuties:
    #     ab_moves[a_diff] = []
    #     ab_time[a_diff] = []
    #
    # for a_diff in a_difficuties:
    #     for i in range(0, iter):
    #         print(a_diff, "-", i)
    #         p1 = BotPlayer(PLAYER_ONE, a_diff, use_alpha_beta=False)
    #         p2 = BotPlayer(PLAYER_TWO, a_diff, use_alpha_beta=False)
    #         game = Mancala(p1, p2)
    #         start = time.time()
    #         AIvsAI(game, True)
    #         stop = time.time()
    #         ab_time[a_diff].append(stop - start)
    #         p1_points, p2_points = game.sum_points()
    #         ab_moves[a_diff].append(p2.moves_to_win if not p1_points > p2_points else p1.moves_to_win)
    #
    # ab_t = []
    # ab_m = []
    # for a_diff in a_difficuties:
    #     ab_t.append(mean(ab_time[a_diff]))
    #     ab_m.append(mean(ab_moves[a_diff]))
    #
    # create_plot({"x": a_difficuties, "min-max": ab_t, "alpha-beta": t}, "Czas rozgrywki(h1)",
    #             "Poziom trudności (głębokość drzewa)", "Czas", "assets/plot2_not_random.png")
    #
    # f = open("assets/h1_vs_h2_not_random.txt", "w")
    #
    # for i in range(0, len(ab_m)):
    #     f.write(f"\nLVL {a_difficuties[i]}: min-max({ab_m[i]}), alpha-beta({m[i]})")
    # f.close()

    return list(zip(t, m)), list(zip(t, m))
