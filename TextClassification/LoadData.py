import random

from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np


def get_sets(train_percentage, verified_percentage):
    texts1 = open("scaledata/Dennis+Schwartz/subj.Dennis+Schwartz", "r")
    texts2 = open("scaledata/James+Berardinelli/subj.James+Berardinelli", "r")
    texts3 = open("scaledata/Scott+Renshaw/subj.Scott+Renshaw", "r")
    texts4 = open("scaledata/Steve+Rhodes/subj.Steve+Rhodes", "r")

    raw_labels1 = open("scaledata/Dennis+Schwartz/label.3class.Dennis+Schwartz", "r")
    raw_labels2 = open("scaledata/James+Berardinelli/label.3class.James+Berardinelli", "r")
    raw_labels3 = open("scaledata/Scott+Renshaw/label.3class.Scott+Renshaw", "r")
    raw_labels4 = open("scaledata/Steve+Rhodes/label.3class.Steve+Rhodes", "r")

    lines = texts1.readlines()
    lines.extend(texts2.readlines())
    lines.extend(texts3.readlines())
    lines.extend(texts4.readlines())

    labels = raw_labels1.readlines()
    labels.extend(raw_labels2.readlines())
    labels.extend(raw_labels3.readlines())
    labels.extend(raw_labels4.readlines())

    return get_training_and_test_set(lines, labels, train_percentage)


def predict_svm(X_train, Y_train, X_test, Y_test):
    text_clf = Pipeline([
        ('vect', CountVectorizer(stop_words='english')),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',
                              alpha=1e-3, random_state=42,
                              max_iter=5, tol=None)),
    ])

    text_clf.fit(X_train, Y_train)
    predicted = text_clf.predict(X_test)
    print(np.mean(predicted == Y_test))


def get_training_and_test_set(lines, labels, percentage=0.9):
    zipped = list(zip(lines, labels))

    random.shuffle(zipped)

    x = len(zipped)
    a = int(x * percentage)
    train_set_zipped = zipped[:a]
    test_set_zipped = zipped[a:]

    return list(zip(*train_set_zipped)), list(zip(*test_set_zipped))


def get_vocabulary(words):
    d = {}

    for word in words:
        if word not in d:
            d[word] = 0
        else:
            d[word] += 1

    return d


def trim_vocabulary(vocabulary, top_offset, bottom_offset):
    l = len(vocabulary.keys())
    new_d = {}
    for key in vocabulary.keys():
        if l * bottom_offset > vocabulary[key] or vocabulary[key] > l * top_offset:
            new_d[key] = vocabulary[key]

    return new_d
