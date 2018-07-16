# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 06:28:24 2016

@author: hina
"""

import glob
import codecs
import numpy
from pandas import DataFrame
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score

# To use the Health data set, uncomment the next 4 lines
SOURCES = [
    ('HealthProNonPro/NonPro/*.txt',  'BAD'),
    ('HealthProNonPro/Pro/*.txt',  'GOOD')
]

# To use the Movie data set, uncomment the next 4 lines
#SOURCES = [
#    ('MoviePosNeg/neg/*.txt',  'BAD'),
#    ('MoviePosNeg/pos/*.txt',  'GOOD')
#]

# read documents from corpus
def read_files (path):
    files = glob.glob(path)
    for file in files:
        # use Unicode text encoding and ignore any errors 
        with codecs.open(file, "r", encoding='utf-8', errors='ignore') as f:
            text = f.read()
            text = text.replace('\n', ' ')
            yield file, text

# put corpus in data frame format for easy manipulation
def build_data_frame(path, classification):
    rows = []
    index = []
    for file_name, text in read_files(path):
        rows.append({'text': text, 'class': classification})
        index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame

# read the corpus data
data = DataFrame({'text': [], 'class': []})
for path, classification in SOURCES:
    data = data.append(build_data_frame(path, classification))

# randomize corpus data
data = data.reindex(numpy.random.permutation(data.index))

# create the data trasformation and classification pipeline 
# http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
# http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
# http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
pipeline = Pipeline([
    ('vect',    CountVectorizer(input = 'content', encoding = 'utf-8', stop_words=None, lowercase=True, binary = False)),
    ('tfidf',   TfidfTransformer(use_idf=False, norm=None)),
    ('clf',     MultinomialNB(alpha=1.0, fit_prior=False, class_prior=None))
])

# do k-fold cross-validation  
# https://en.wikipedia.org/wiki/Cross-validation_(statistics)
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.KFold.html
k_fold = KFold(n=len(data), n_folds=6)
scores = []
confusion = numpy.array([[0, 0], [0, 0]])
for train_indices, test_indices in k_fold:
    train_text = data.iloc[train_indices]['text'].values
    train_y = data.iloc[train_indices]['class'].values.astype(str)

    test_text = data.iloc[test_indices]['text'].values
    test_y = data.iloc[test_indices]['class'].values.astype(str)

    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label='GOOD')
    scores.append(score)

# print the accuracy and confusion matrix of classification
print('Total documents classified:', len(data))
print('Score:', round(sum(scores)/len(scores),2))
print('Confusion matrix:')
print(confusion)

