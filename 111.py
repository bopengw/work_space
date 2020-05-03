from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()

import numpy as np
corpus = [
         'This is the first document',
         'This is the second second document',
         'And the third one',
         'Is this the first document?']

def get_all_word(corpus):
    words = []
    corpus_split = []
    for line in corpus:
        line_split = line.split(" ")
        words.extend(line_split)
        corpus_split.append(line_split)
    words = {}.fromkeys(words).keys()
    return list(words), corpus_split

def get_matrix(words, corpus_split):
    val = np.zeros(len(words))
    matrix = []
    for vec in corpus_split:
        dictory = dict(zip(words, val))
        for element in vec:
            dictory[element] += 1
        matrix.append(list(dictory.values()))
    return np.array(matrix)


words, corpus_split = get_all_word(corpus)
matrix = get_matrix(words, corpus_split)
print(words, corpus)
print(matrix)