import random

from sklearn import svm
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np


def get_sets(class_num=3):
    texts1 = open("scaledata/Dennis+Schwartz/subj.Dennis+Schwartz", "r")
    texts2 = open("scaledata/James+Berardinelli/subj.James+Berardinelli", "r")
    texts3 = open("scaledata/Scott+Renshaw/subj.Scott+Renshaw", "r")
    texts4 = open("scaledata/Steve+Rhodes/subj.Steve+Rhodes", "r")

    raw_labels1 = open(f"scaledata/Dennis+Schwartz/label.{class_num}class.Dennis+Schwartz", "r")
    raw_labels2 = open(f"scaledata/James+Berardinelli/label.{class_num}class.James+Berardinelli", "r")
    raw_labels3 = open(f"scaledata/Scott+Renshaw/label.{class_num}class.Scott+Renshaw", "r")
    raw_labels4 = open(f"scaledata/Steve+Rhodes/label.{class_num}class.Steve+Rhodes", "r")

    lines = texts1.readlines()
    lines.extend(texts2.readlines())
    lines.extend(texts3.readlines())
    lines.extend(texts4.readlines())

    labels = raw_labels1.readlines()
    labels.extend(raw_labels2.readlines())
    labels.extend(raw_labels3.readlines())
    labels.extend(raw_labels4.readlines())

    return lines, labels


def predict_svm(X_train, Y_train, X_test, Y_test, **kwargs):
    text_clf = Pipeline([
        ('vect', CountVectorizer(stop_words='english',
                                 max_features=kwargs['max_features'] if 'max_features' in kwargs else None)),
        ('tfidf', TfidfTransformer()),
        ('clf', svm.SVC(kernel='linear')),
    ])

    if 'max_features' in kwargs:
        del kwargs['max_features']

    text_clf.set_params(**kwargs)
    text_clf.fit(X_train, Y_train)
    predicted = text_clf.predict(X_test)
    return np.mean(predicted == Y_test)


def predict_bayes(X_train, Y_train, X_test, Y_test, **kwargs):
    text_clf = Pipeline([
        ('vect', CountVectorizer(stop_words='english', max_features=kwargs['max_features'] if 'max_features' in kwargs else None)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB(alpha=kwargs['alpha'], fit_prior=kwargs['fit_prior'])),
    ])
    if 'max_features' in kwargs:
        del kwargs['max_features']

    text_clf.fit(X_train, Y_train)
    predicted = text_clf.predict(X_test)
    return np.mean(predicted == Y_test)


def get_training_and_test_set(lines, labels, percentage=0.9, max_data=5000):
    zipped = list(zip(lines, labels))
    random.shuffle(zipped)
    zipped = zipped[:max_data]
    x = len(zipped)
    a = int(x * percentage)
    train_set_zipped = zipped[:a]
    test_set_zipped = zipped[a:]

    return list(zip(*train_set_zipped)), list(zip(*test_set_zipped))


def pick_train_and_test_sets(X, Y, k, nfolds, max_data):
    sets = split_sets_to_smaller_pieces(X, Y, nfolds, max_data)
    X_train = []
    Y_train = []
    X_test = []
    Y_test = []

    for i in range(len(sets)):
        if i != k:
            X_train.extend(sets[i][0])
            Y_train.extend(sets[i][1])
        else:
            X_test.extend(sets[i][0])
            Y_test.extend(sets[i][1])

    return X_train, Y_train, X_test, Y_test


def tuning_hyper_parameters_nb(X, Y, alphas, fit_priors, nfolds):
    best_params = alphas[0], fit_priors[0]
    best = np.inf * -1
    print("NB")

    for alpha in alphas:
        for fit_prior in fit_priors:
            vals = []
            for i in range(0, nfolds):
                X_train, Y_train, X_text, Y_test = pick_train_and_test_sets(X, Y, i, nfolds, 5000)
                params = {'alpha': alpha, 'fit_prior': fit_prior}
                vals.append(predict_bayes(X_train, Y_train, X_text, Y_test, **params))

            val = np.mean(vals)
            print(alpha, fit_prior, val)
            if val > best:
                best = val
                print(best)
                best_params = {'alpha': alpha, 'fit_prior': fit_prior}

    return best_params




def tuning_hyper_parameters_svm(X, Y, cs, gammas, nfolds):
    best_params = {}
    best = np.inf * -1
    print("SVM")
    for c in cs:
        for gamma in gammas:
            vals = []
            params = {'clf__C': c, 'clf__gamma': gamma}
            for i in range(0, nfolds):
                X_train, Y_train, X_text, Y_test = pick_train_and_test_sets(X, Y, i, nfolds, 5000)
                vals.append(predict_svm(X_train, Y_train, X_text, Y_test, **params))
            val = np.mean(vals)
            print(c, gamma, val)
            if val > best:
                best = val
                best_params = params

    return best_params


def split_sets_to_smaller_pieces(X, Y, k, max_data):
    zipped = list(zip(X, Y))
    random.shuffle(zipped)
    zipped = zipped[:max_data]
    length = len(zipped)
    part = int(length / k)
    parts = []
    for i in range(1, k + 1):
        parts.append(zipped[part * (i - 1):i * part])

    return list(map(lambda _x: list(zip(*_x)), parts))


def test_cross(X, Y, f, nfolds, max_data, **kwargs):
    vals = []
    for i in range(0, nfolds):
        X_train, Y_train, X_text, Y_test = pick_train_and_test_sets(X, Y, i, nfolds, max_data)
        vals.append(f(X_train, Y_train, X_text, Y_test, **kwargs))

    return np.mean(vals)
