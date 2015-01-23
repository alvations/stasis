#!/usr/bin/env python -*- coding: utf-8 -*-

import io, os,re

import sys; reload(sys); sys.setdefaultencoding("utf-8")

STS2012_TRAIN = {'STS.input.MSRpar.txt':'STS.gs.MSRpar.txt',
                 'STS.input.SMTeuroparl.txt':'STS.gs.SMTeuroparl.txt',
                 'STS.input.MSRvid.txt':'STS.gs.MSRvid.txt'}

STS2012_GOLD = {'STS.input.MSRpar.txt': 'STS.gs.MSRpar.txt',
                'STS.input.MSRvid.txt':'STS.gs.MSRvid.txt', 
                'STS.input.surprise.SMTnews.txt': 'STS.gs.surprise.SMTnews.txt',
                'STS.input.SMTeuroparl.txt':'STS.gs.SMTeuroparl.txt',
                'STS.input.surprise.OnWN.txt': 'STS.gs.surprise.OnWN.txt'}

STS2013_GOLD = {'STS.input.SMT.txt':'STS.gs.SMT.txt', 
                'STS.input.OnWN.txt':'STS.gs.OnWN.txt',
                'STS.input.headlines.txt':'STS.gs.headlines.txt',
                'STS.input.FNWN.txt':'STS.gs.FNWN.txt'}

STS2014_GOLD = {'STS.input.deft-news.txt': 'STS.gs.deft-news.txt', 
                'STS.input.images.txt':'STS.gs.images.txt',
                'STS.input.deft-forum.txt':'STS.gs.deft-forum.txt',
                'STS.input.OnWN.txt':'STS.gs.OnWN.txt',
                'STS.input.headlines.txt': 'STS.gs.headlines.txt',
                'STS.input.tweet-news.txt': 'STS.gs.tweet-news.txt'}

STS2015_GOLD = {'STS.input.answers-forums.txt':'STS.gs.answers-forums.txt', 
                'STS.input.images.txt':'STS.gs.images.txt',
                'STS.input.answers-students.txt':'STS.gs.answers-students.txt', 
                'STS.input.headlines.txt':'STS.gs.headlines.txt', 
                'STS.input.belief.txt':'STS.gs.belief.txt'}


STS_DATA_DIR = 'STS-data/'
ALL_STS_DATA = {'STS2012-train/':STS2012_TRAIN,'STS2012-gold/':STS2012_GOLD,
                'STS2013-gold/':STS2013_GOLD, 'STS2014-gold/':STS2014_GOLD,
                'STS2015-gold/':STS2015_GOLD}

def create_allinone_csv_file():
    fout = io.open('sts.csv', 'w')
    for dataset in sorted(ALL_STS_DATA):
        for inputfile, goldstandard in ALL_STS_DATA[dataset].iteritems():
            inputfile = STS_DATA_DIR + dataset + inputfile
            goldstandard = STS_DATA_DIR + dataset + goldstandard
            domain = ".".join(inputfile.split('.')[2:-1])
            with io.open(inputfile, 'r') as infile, io.open(goldstandard, 'r') as goldfile:
                for line, score in zip(infile, goldfile):
                    left, right = line.strip().split('\t')
                    score = score.strip()
                    outline = "\t".join([dataset[:-1], domain, score, left, right])
                    fout.write(unicode(outline)+'\n')
