#!/usr/bin/env python -*- coding: utf-8 -*-

import io

from nltk import word_tokenize, pos_tag
from nltk.util import ngrams

with io.open('sts.csv', 'r', encoding='utf8') as fin:
    for line in fin:
        dataset, domain, score, left, right = line.strip().split('\t')
        print left, right
