import sys, string
import array
import math
import time

import graphlab as gl
from graphlab.toolkits.distances import cosine
import numpy as np
import pandas as pd
from nltk.corpus import stopwords

try:
    import cPickle as pickle
except:
    import pickle


punct = string.punctuation
sts = gl.SFrame('sts_all.gl/')
stoplist = set(stopwords.words('english'))

def get_embeddings(embedding_gzip, size):
    headers = ['word'] + ['d'+str(i) for i in range(1, size+1)]
    coltypes = [str] + [float] * size
    sf = gl.SFrame.read_csv( embedding_gzip, delimiter=' ', column_type_hints=coltypes, header=False, quote_char='\0')
    sf = sf.pack_columns(['X'+str(i) for i in range(2, size+1)])
    df = sf.to_dataframe().set_index('X1')
    column_names = list(df)
    return df.to_dict(orient='dict')[column_names[1]]


#content_vocab = set(i.strip() for i in open('sts_vocab.txt', 'r').readlines())

def get_vector(word, embeddings):
    return np.array(embeddings[word])

def sent_vector(words, embeddings):
    _lemmas = [w for w in words if w in embeddings and w not in stoplist]
    _sum = sum(np.array(embeddings[l]) for l in _lemmas) / len(words)
    return _sum


def cosine(v1, v2):
    v1_abs = math.sqrt(np.dot(v1, v1))
    v2_abs = math.sqrt(np.dot(v2, v2))
    cosine_output = np.dot(v1, v2) / (v1_abs * v2_abs)
    if type(cosine_output) == np.float64:
        return cosine_output
    else:
        return -1.0




estart = time.time()
glove = get_embeddings('glove-vectors/glove.840B.300d.txt', 300)
print "Embeddings loaded, took:", time.time() - estart

sent1_lemmatized = sts['Sent1_lemmatized']
sent2_lemmatized = sts['Sent2_lemmatized']
sts = None

fout = open('sts_glove.csv', 'w')
fout.write('glove_cosine'+ '\n')
for s1, s2 in zip(sent1_lemmatized, sent2_lemmatized):
    s1 = eval(s1)
    s2 = eval(s2)
    v1 = sent_vector(s1, glove)
    v2 = sent_vector(s2, glove)
    fout.write(str(cosine(v1, v2)) + '\n')
