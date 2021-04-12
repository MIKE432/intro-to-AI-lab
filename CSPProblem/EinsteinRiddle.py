from random import randint
from typing import List

from EinsteinConsts import *
from abstracts.Problem import Problem
from abstracts.Variable import Variable


def init_einstein_problem():
    main_domain = [0, 1, 2, 3, 4]
    problem = EinsteinRiddle(main_domain)

    # colors
    red = EinsteinVariable(-1, main_domain, COLOR_RED)
    green = EinsteinVariable(-1, main_domain, COLOR_GREEN)
    yellow = EinsteinVariable(-1, main_domain, COLOR_YELLOW)
    blue = EinsteinVariable(-1, main_domain, COLOR_BLUE)
    white = EinsteinVariable(-1, main_domain, COLOR_WHITE)
    colors = [red, green, yellow, blue, white]

    # nationalities
    norwegian = EinsteinVariable(-1, [FIRST_HOUSE], NATIONALITY_NORWEGIAN)
    english = EinsteinVariable(-1, main_domain, NATIONALITY_ENGLISH)
    dutch = EinsteinVariable(-1, main_domain, NATIONALITY_DUTCH)
    german = EinsteinVariable(-1, main_domain, NATIONALITY_GERMAN)
    swedish = EinsteinVariable(-1, main_domain, NATIONALITY_SWEDISH)
    nationalities = [norwegian, english, dutch, swedish, german]

    # smoke
    light = EinsteinVariable(-1, main_domain, SMOKE_LIGHT)
    cigar = EinsteinVariable(-1, main_domain, SMOKE_CIGAR)
    pipe = EinsteinVariable(-1, main_domain, SMOKE_PIPE)
    no_filter = EinsteinVariable(-1, main_domain, SMOKE_NO_FILTER)
    menthol = EinsteinVariable(-1, main_domain, SMOKE_MENTHOL)
    smoke = [light, cigar, pipe, no_filter, menthol]

    # drinks
    tea = EinsteinVariable(-1, main_domain, DRINK_TEA)
    water = EinsteinVariable(-1, main_domain, DRINK_WATER)
    milk = EinsteinVariable(-1, [THIRD_HOUSE], DRINK_MILK)
    beer = EinsteinVariable(-1, main_domain, DRINK_BEER)
    coffee = EinsteinVariable(-1, main_domain, DRINK_COFFEE)
    drinks = [tea, water, milk, beer, coffee]

    # pets
    cats = EinsteinVariable(-1, main_domain, PET_CATS)
    birds = EinsteinVariable(-1, main_domain, PET_BIRDS)
    dogs = EinsteinVariable(-1, main_domain, PET_DOGS)
    horses = EinsteinVariable(-1, main_domain, PET_HORSES)
    fishes = EinsteinVariable(-1, main_domain, PET_FISHES)
    pets = [cats, birds, dogs, horses, fishes]

    problem.add_node(red)
    problem.add_node(green)
    problem.add_node(yellow)
    problem.add_node(blue)
    problem.add_node(white)

    problem.add_node(norwegian)
    problem.add_node(english)
    problem.add_node(dutch)
    problem.add_node(german)
    problem.add_node(swedish)

    problem.add_node(light)
    problem.add_node(cigar)
    problem.add_node(pipe)
    problem.add_node(no_filter)
    problem.add_node(menthol)

    problem.add_node(tea)
    problem.add_node(water)
    problem.add_node(milk)
    problem.add_node(beer)
    problem.add_node(coffee)

    problem.add_node(cats)
    problem.add_node(birds)
    problem.add_node(dogs)
    problem.add_node(horses)
    problem.add_node(fishes)

    # neighbours
    red.add_neighbour(english)
    english.add_neighbour(red)

    dutch.add_neighbour(tea)
    tea.add_neighbour(dutch)

    yellow.add_neighbour(cigar)
    cigar.add_neighbour(yellow)

    german.add_neighbour(pipe)
    pipe.add_neighbour(german)

    no_filter.add_neighbour(birds)
    birds.add_neighbour(no_filter)

    swedish.add_neighbour(dogs)
    dogs.add_neighbour(swedish)

    menthol.add_neighbour(beer)
    beer.add_neighbour(menthol)

    green.add_neighbour(coffee)
    coffee.add_neighbour(green)

    # 3
    green.add_neighbour(white)
    white.add_neighbour(green)

    # 5
    light.add_neighbour(cats)
    cats.add_neighbour(light)

    # 9
    light.add_neighbour(water)
    water.add_neighbour(light)

    # 12
    norwegian.add_neighbour(blue)
    blue.add_neighbour(norwegian)

    for x in colors:
        for y in colors:
            if x != y and y not in x.neighbours:
                x.add_neighbour(y)

    for x in nationalities:
        for y in nationalities:
            if x != y and y not in x.neighbours:
                x.add_neighbour(y)

    for x in smoke:
        for y in smoke:
            if x != y and y not in x.neighbours:
                x.add_neighbour(y)

    for x in drinks:
        for y in drinks:
            if x != y and y not in x.neighbours:
                x.add_neighbour(y)

    for x in pets:
        for y in pets:
            if x != y and y not in x.neighbours:
                x.add_neighbour(y)

    return problem


class EinsteinVariable(Variable):
    def __init__(self, def_val, domain: List, about):
        super().__init__(def_val, domain)
        self.about = about


class EinsteinRiddle(Problem):
    def __init__(self, domain):
        super().__init__(domain)
        self.__prev = 0

    def next(self):
        return self.__find_next_empty_node()

    def __find_next_empty_node(self):
        for i in range(0, len(self.nodes)):
            if not self.nodes[i].is_value_changed():
                return self.nodes[i]
        return None
