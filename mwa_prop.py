from __future__ import division

import graphlab
from itertools import chain
import string

from nltk import word_tokenize

import os
import sys

#graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 20)

testfile = 'sts2016-test.clean.csv'

sts_test = graphlab.SFrame.read_csv(testfile, delimiter='\t', column_type_hints=[str, str, str, str], quote_char='\0')
mwa_test = graphlab.SFrame.read_csv('sts2016-test.mwa.csv', delimiter='\t', column_type_hints=[str,str], quote_char='\0')
sts_test['Sent1_tokenized']  = graphlab.text_analytics.tokenize(sts_test['Sent1'], to_lower=False)
sts_test['Sent2_tokenized']  = graphlab.text_analytics.tokenize(sts_test['Sent2'], to_lower=False)

# Sultan et al. 2014

stoplist = graphlab.text_analytics.stopwords(lang='en')
punctuations = string.punctuation
stoplist.update(set(punctuations))
C = set(w.strip(punctuations).lower() for w in chain(*sts_test['Sent1_tokenized']) if w not in stoplist)
C.remove('')
C2 = set(w.strip(punctuations).lower() for w in chain(*sts_test['Sent2_tokenized']) if w not in stoplist)
C2.remove('')
C.update(C2)

def content_num(row, idx):
    if row == 'None':
        return 0
    else:
        return sum(1 for wordpair in eval(row) if wordpair[0] in C)


numerator_s1 = mwa_test.apply(lambda x: content_num(x['MWA_Word'], 0))
denominator_s1 = sts_test.apply(lambda x: sum(1 for w in x['Sent1_tokenized'] if w in C))

numerator_s2 = mwa_test.apply(lambda x: content_num(x['MWA_Word'], 1))
denominator_s2 = sts_test.apply(lambda x: sum(1 for w in x['Sent2_tokenized'] if w in C))

#print len(numerator_s1), len(denominator_s1), len(numerator_s2), len(denominator_s2)

mwa_prop = graphlab.SFrame({'n_s1': numerator_s1 , 'd_s1': denominator_s1,
                           'n_s2': numerator_s2, 'd_s2': denominator_s2})

mwa_prop['prop_s1'] = mwa_prop.apply(lambda x: x['n_s1'] / (x['d_s1'] + 1))
mwa_prop['prop_s2'] = mwa_prop.apply(lambda x: x['n_s2'] / (x['d_s2'] + 1))

def harmonic(x, e):
    return (2*x['prop_s1']*x['prop_s1']) /(x['prop_s1'] + x['prop_s2'] + e)

epsilon = 1
mwa_prop['prop_harmonic'] = mwa_prop.apply(lambda x: harmonic(x, epsilon))

sts_test.add_column(mwa_prop['prop_harmonic'], name='prop_harmonic')

sts_test.save('mwa_test/'+testfile+'.csv', format='csv')
