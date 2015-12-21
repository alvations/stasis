#!/usr/bin/env python3 -*- coding: utf-8 -*-

import io
import os
import re

para2sent = {
'data/training/paragraph2sentence.train.input.tsv': 
('keys/training/paragraph2sentence.train.gs.tsv', 
'keys/baselines/paragraph2sentence.training.baseline.tsv'),
		
'data/test/paragraph2sentence.test.input.tsv': 
('keys/test/paragraph2sentence.test.gs.tsv', 
'keys/baselines/paragraph2sentence.test.baseline.tsv'), 
		
'data/test/paragraph2sentence.trial.input.tsv':
('keys/trial/paragraph2sentence.trial.gs.tsv', '')}


sent2phrase = {
'data/training/sentence2phrase.train.input.tsv': 
('keys/training/sentence2phrase.train.gs.tsv', 
'keys/baselines/sentence2phrase.training.baseline.tsv'),
		
'data/test/sentence2phrase.test.input.tsv': 
('keys/test/sentence2phrase.test.gs.tsv', 
'keys/baselines/sentence2phrase.test.baseline.tsv'), 
		
'data/test/sentence2phrase.trial.input.tsv':
('keys/trial/sentence2phrase.trial.gs.tsv', '')}



phrase2word = {
'data/training/phrase2word.train.input.tsv': 
('keys/training/phrase2word.train.gs.tsv', 
'keys/baselines/phrase2word.training.baseline.tsv'),
		
'data/test/phrase2word.test.input.tsv': 
('keys/test/phrase2word.test.gs.tsv', 
'keys/baselines/phrase2word.test.baseline.tsv'), 
		
'data/test/phrase2word.trial.input.tsv':
('keys/trial/phrase2word.trial.gs.tsv', '')}


word2sense = {
'data/training/word2sense.train.input.tsv': 
('keys/training/word2sense.train.gs.tsv', 
'keys/baselines/word2sense.training.baseline.tsv'),
		
'data/test/word2sense.test.input.tsv': 
('keys/test/word2sense.test.gs.tsv', 
'keys/baselines/word2sense.test.baseline.tsv'), 
		
'data/test/word2sense.trial.input.tsv':
('keys/trial/word2sense.trial.gs.tsv', '')}


CLSS_DATA_DIR = 'CLSS-data/'
ALL_CLSS_TEXT_DATA = [para2sent, sent2phrase, phrase2word]

def create_allinone_csv_file():
    fout = io.open('clss-text.csv', 'w')
    headerline = "\t".join(['Dataset', 'Level1', 'Level2', 'Genre', 'Baseline', 'Score'])
    fout.write(unicode(headerline)+'\n')
    for crosslevel in sorted(ALL_CLSS_TEXT_DATA):
    	for dataset in sorted(crosslevel):
    		dataset_name = '.'.join(dataset.split('/')[-1].split('.')[:2])
    		scorefile, baselinefile = crosslevel[dataset]
    		#print dataset, '\t', scorefile
    		scores = [i.strip() for i in open(CLSS_DATA_DIR+scorefile)]
    		if not baselinefile:
    			baselines = [''] * len(scores)
    		else:
    			baselines= [i.strip() for i in open(CLSS_DATA_DIR+baselinefile)]
			for line, baseline, score, in zip(io.open(CLSS_DATA_DIR+dataset, 'r', encoding='utf8'), baselines, scores):
				level1, level2, genre = line.strip().split('\t')
				genre, clssid = genre.split('-') # clssid is not very useful to tasks outside semeval2013.
				score = str(round(float(score) * 5 / 4 , 2))
				baseline = str(round(float(baseline) * 5 / 4 , 2))
				outline = '\t'.join([dataset_name, level1, level2, genre, baseline, score])
				fout.write(unicode(outline)+'\n')
    		
create_allinone_csv_file()


