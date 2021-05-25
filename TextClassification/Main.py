from LoadData import get_sets, predict_svm, get_training_and_test_set, split_sets_to_smaller_pieces, \
    tuning_hyper_parameters_svm, tuning_hyper_parameters_nb

if __name__ == '__main__':
    X, Y = get_sets()
    s = split_sets_to_smaller_pieces(X, Y, 10)
    Cs = [0.001, 0.01, 0.1, 1, 10]
    gammas = [0.001, 0.01, 0.1, 1]
    # tuning_hyper_parameters_svm(X, Y, Cs, gammas, 10)
    tuning_hyper_parameters_nb(X, Y, [0.01, 0.1, 0.2, 0.5, 0.7, 0.9, 1.0], [True, False], 10)
    [X_train, Y_train], [X_test, Y_test] = get_training_and_test_set(X, Y)
    predict_svm(X_train, Y_train, X_test, Y_test)

