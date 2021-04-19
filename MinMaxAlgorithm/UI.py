import pygame

from implementations.Mancala import Mancala


def init(game: Mancala):
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
