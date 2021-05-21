from LoadData import get_sets, predict_svm

if __name__ == '__main__':
    [X_train, Y_train], [X_test, Y_test] = get_sets(0.9, 0.2)
    predict_svm(X_train, Y_train, X_test, Y_test)
