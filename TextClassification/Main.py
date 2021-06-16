from LoadData import get_sets, predict_svm, get_training_and_test_set, split_sets_to_smaller_pieces, \
    tuning_hyper_parameters_svm, tuning_hyper_parameters_nb, test_cross, predict_bayes
import numpy as np

Cs = [0.5, 0.75, 1, 1.25]
gammas = [0.75, 1, 1.5]
max_features = [50, 500, 1000, 2000, 4000, 8000, 16000, 32000]


def test_hyperparameters():
    X, Y = get_sets()
    best_nb = tuning_hyper_parameters_nb(X, Y, [0.01, 0.1, 0.2, 0.5, 0.7, 0.9, 1.0], [True, False], 10)
    best_svm = tuning_hyper_parameters_svm(X, Y, Cs, gammas, 10)


def test_features_number(best_svm, best_nb):
    print("TEST FEATURES NUMBER")
    X, Y = get_sets()
    for max_f in max_features:
        best_svm['max_features'] = max_f
        best_nb['max_features'] = max_f
        print(f"nb + {max_f}", test_cross(X, Y, predict_bayes, 10, **best_nb))
        print(f"svm + {max_f}", test_cross(X, Y, predict_svm, 10, **best_svm))


def test_validation_set(best_svm, best_nb):
    X, Y = get_sets()

    [X_train, Y_train], [X_test, Y_test] = get_training_and_test_set(X, Y)
    # best_nb_val = tuning_hyper_parameters_nb(X_train, Y_train, [0.01, 0.1, 0.2, 0.5, 0.7, 0.9, 1.0], [True, False], 10)
    # # best_svm_val = tuning_hyper_parameters_svm(X_train, Y_train, Cs, gammas, 10)
    #
    # best_nb = tuning_hyper_parameters_nb(X, Y, [0.01, 0.1, 0.2, 0.5, 0.7, 0.9, 1.0], [True, False], 10)
    # best_svm = tuning_hyper_parameters_svm(X, Y, Cs, gammas, 10)
    # print(best_nb, best_nb_val)
    # print(f"nb-val", predict_bayes(X_train + X_test, Y_train + Y_test, X_test, Y_test, **best_nb),
    #       predict_bayes(X_train, Y_train, X_test, Y_test, **best_nb))
    # print(f"svm-val", predict_svm(X_train, Y_train, X_test, Y_test, **best_svm),
    #       predict_svm(X_train, Y_train, X_test, Y_test, **best_svm_val))


def test_data_amount():
    X, Y = get_sets()
    for i in [500, 1000, 2000, 3000, 4000, 5000]:
        print(f"{i} svm:", test_cross(X, Y, predict_svm, 10, i, **{'clf__C': 1, 'clf__gamma': 'scale'}),
              "bayes:", test_cross(X, Y, predict_bayes, 10, i, **{'alpha': 0.1, 'fit_prior': False}))


def different_kernels():
    X, Y = get_sets()
    tuning_hyper_parameters_svm(X, Y, Cs, gammas, 10)
    #
    # X, Y = get_sets()
    # tuning_hyper_parameters_svm(X, Y, Cs, gammas, 10)


if __name__ == '__main__':
    # test_hyperparameters()
    # test_validation_set({'clf__C': 1, 'clf__gamma': 'scale'}, {'alpha': 0.1, 'fit_prior': False})
    # test_data_amount()
    different_kernels()