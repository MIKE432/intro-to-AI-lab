# ------------------------------------------------------
# --------------------- SPLITTERS ----------------------
FIRST_SPLITTER = ";"
SECOND_SPLITTER = ","
# ------------------------------------------------------


# ------------------------------------------------------
# --------------------- PENALTIES ----------------------
SUM_OUT_OF_BOARD_PENALTY = 15.5
OUT_OF_BOARD_PENALTY = 7.5
INTERSECTIONS_PENALTY = 45
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
CLOSER_PROBABILITY = 3
# --------------------------------------------------------

# --------------------------------------------------------
# ---------------------- INIT CONFIG ---------------------
BEST_INIT_ITERATION = 5
# --------------------------------------------------------


FILE = "test_file2"
POPULATION_NUMBER = 500
TOURNAMENT_SIZE = int(POPULATION_NUMBER/4)
CROSS_PROBABILITY = 0.2
INHERIT_PARENT = 0  # left parent(0) right(1)
MUTATE_MOVE = 2
PATH_MUTATION_PROBABILITY = 0.2
EPOCHS_WITHOUT_BEST = 15

JSON_FILE = "assets/solution_to_print.json"
OUTPUT = "assets/output.png"
