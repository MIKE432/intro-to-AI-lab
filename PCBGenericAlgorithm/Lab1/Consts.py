# ------------------------------------------------------
# --------------------- SPLITTERS ----------------------
FIRST_SPLITTER = ";"
SECOND_SPLITTER = ","
# ------------------------------------------------------


# ------------------------------------------------------
# --------------------- PENALTIES ----------------------
SUM_OUT_OF_BOARD_PENALTY = 115.5
OUT_OF_BOARD_PENALTY = 15
INTERSECTIONS_PENALTY = 50
# --------------------------------------------------------


# --------------------------------------------------------
# --------------------- DIRECTIONS -----------------------
TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3
# --------------------------------------------------------


# --------------------------------------------------------
# --------------------- PROBABILITIES --------------------
CLOSER_PROBABILITY = 1.7
# --------------------------------------------------------

# --------------------------------------------------------
# ---------------------- INIT CONFIG ---------------------
BEST_INIT_ITERATION = 5
# --------------------------------------------------------


FILE = "test_file3"
POPULATION_NUMBER = 200
TOURNAMENT_SIZE = int(POPULATION_NUMBER/5)
CROSS_PROBABILITY = 0.35
INHERIT_PARENT = 0
MUTATE_MOVE = 1
PATH_MUTATION_PROBABILITY = 0.15
EPOCHS_WITHOUT_BEST = 50

JSON_FILE = "assets/solution_to_print.json"
OUTPUT = "assets/output.png"
