#!/usr/bin/env python3 -*- coding: utf-8 -*-

import io
import os
import re

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

STS2016_GOLD = {'STS2016.input.answer-answer.txt': 'STS2016.gs.answer-answer.txt',
                'STS2016.input.headlines.txt': 'STS2016.gs.headlines.txt',
                'STS2016.input.plagiarism.txt': 'STS2016.gs.plagiarism.txt',
                'STS2016.input.postediting.txt': 'STS2016.gs.postediting.txt',
                'STS2016.input.question-question.txt': 'STS2016.gs.question-question.txt' }


STS_DATA_DIR = 'STS-data/'
ALL_STS_DATA = {'STS2012-train/':STS2012_TRAIN,'STS2012-gold/':STS2012_GOLD,
                'STS2013-gold/':STS2013_GOLD, 'STS2014-gold/':STS2014_GOLD,
                'STS2015-gold/':STS2015_GOLD, 'STS2016-gold/':STS2016_GOLD}

def clean(text):
    text = text.replace(u"�", "e").replace(u'”', '"').replace(u'“', '')
    text = text.replace(u"\x92", "'").replace(u"\x91", "").replace(u"\x93", "").replace(u"\x94", "").replace(u"\x95", "")
    text = text.replace(u"‚Äôs", "'s").replace(u"Äė", "").replace(u"‚Äė", "").replace(u"‚Äô", "").replace(u"‚Äď", "").replace(u"‚ā¨", "").replace(u"‚ÄĒ", "")
    text = text.replace(u"😢🐶", "")
    return text

def create_allinone_csv_file():
    fout = io.open('sts.csv', 'w')
    headerline = "\t".join(['Dataset', 'Domain', 'Score', 'Sent1', 'Sent2'])
    fout.write(unicode(headerline)+'\n')
    for dataset in sorted(ALL_STS_DATA):
        for inputfile, goldstandard in ALL_STS_DATA[dataset].iteritems():
            inputfile = STS_DATA_DIR + dataset + inputfile
            goldstandard = STS_DATA_DIR + dataset + goldstandard
            domain = ".".join(inputfile.split('.')[2:-1])
            with io.open(inputfile, 'r') as infile, io.open(goldstandard, 'r') as goldfile:
                for line, score in zip(infile, goldfile):
                    if dataset in ['STS2016-gold/']:
                        left, right, left_source, right_source = line.strip().split('\t')
                    else:
                        left, right = line.strip().split('\t')
                    left = left.replace('\t', ' ')
                    right = right.replace('\t', ' ')
                    left = re.sub(' +',' ', left)
                    right = re.sub(' +',' ', right)

                    score = score.strip()
                    outline = "\t".join([dataset[:-1], domain, score, left, right]).strip()

                    fout.write(unicode(outline)+'\n')

create_allinone_csv_file()


"""
# Asiya
nohup $ASIYA_HOME/bin/Asiya.pl -eval single -g seg -m NGRAM-cosChar2ngrams,NGRAM-cosChar3ngrams,NGRAM-cosChar4ngrams,NGRAM-cosChar5ngrams,NGRAM-cosTok2ngrams,NGRAM-cosTok3ngrams,NGRAM-cosTok4ngrams,NGRAM-cosTok5ngrams,NGRAM-jacChar2ngrams,NGRAM-jacChar3ngrams,NGRAM-jacChar4ngrams,NGRAM-jacChar5ngrams,NGRAM-jacCognates,NGRAM-jacTok2ngrams,NGRAM-jacTok3ngrams,NGRAM-jacTok4ngrams,NGRAM-jacTok5ngrams,NGRAM-lenratio assiya.config > ass.ngram.out 2> ass.ngram.out.err &

nohup $ASIYA_HOME/bin/Asiya.pl -eval single -g seg -m "SP-Oc(*),SP-Oc(ADJP),SP-Oc(ADVP),SP-Oc(CONJP),SP-Oc(INTJ),SP-Oc(LST),SP-Oc(NP),SP-Oc(O),SP-Oc(PP),SP-Oc(PRT),SP-Oc(SBAR),SP-Oc(UCP),SP-Oc(VP),SP-cNIST,SP-cNIST-1,SP-cNIST-2,SP-cNIST-3,SP-cNIST-4,SP-cNIST-5,SP-cNISTi-2,SP-cNISTi-3,SP-cNISTi-4,SP-cNISTi-5,SP-iobNIST,SP-iobNIST-1,SP-iobNIST-2,SP-iobNIST-3,SP-iobNIST-4,SP-iobNIST-5,SP-iobNISTi-2,SP-iobNISTi-3,SP-iobNISTi-4,SP-iobNISTi-5,SP-lNIST,SP-lNIST-1,SP-lNIST-2,SP-lNIST-3,SP-lNIST-4,SP-lNIST-5,SP-lNISTi-2,SP-lNISTi-3,SP-lNISTi-4,SP-lNISTi-5,SP-pNIST,SP-pNIST-1,SP-pNIST-2,SP-pNIST-3,SP-pNIST-4,SP-pNIST-5,SP-pNISTi-2,SP-pNISTi-3,SP-pNISTi-4,SP-pNISTi-5" assiya.config > ass.sp.out  2> ass.sp.out.err &

nohup $ASIYA_HOME/bin/Asiya.pl -eval single -g seg -m "NE-Me(*),NE-Me(ANGLE_QUANTITY),NE-Me(DATE),NE-Me(DISTANCE_QUANTITY),NE-Me(LANGUAGE),NE-Me(LOC),NE-Me(MEASURE),NE-Me(METHOD),NE-Me(MISC),NE-Me(MONEY),NE-Me(NUM),NE-Me(ORG),NE-Me(PER),NE-Me(PERCENT),NE-Me(PROJECT),NE-Me(SIZE_QUANTITY),NE-Me(SPEED_QUANTITY),NE-Me(SYSTEM),NE-Me(TEMPERATURE_QUANTITY),NE-Me(TIME),NE-Me(WEIGHT_QUANTITY),NE-Oe(*),NE-Oe(**),NE-Oe(ANGLE_QUANTITY),NE-Oe(DATE),NE-Oe(DISTANCE_QUANTITY),NE-Oe(LANGUAGE),NE-Oe(LOC),NE-Oe(MEASURE),NE-Oe(METHOD),NE-Oe(MISC),NE-Oe(MONEY),NE-Oe(NUM),NE-Oe(O),NE-Oe(ORG),NE-Oe(PER),NE-Oe(PERCENT),NE-Oe(PROJECT),NE-Oe(SIZE_QUANTITY),NE-Oe(SPEED_QUANTITY),NE-Oe(SYSTEM),NE-Oe(TEMPERATURE_QUANTITY),NE-Oe(TIME),NE-Oe(WEIGHT_QUANTITY)" assiya.config > ass.ne.out  2> ass.ne.out.err &

# Meteor
java -jar meteor-1.5.jar left right -norm > meteor-all.out
java -jar meteor-1.5.jar left right -norm -writeAlignments -f sts
java -jar meteor-1.5.jar left right -norm -m exact > meteor-exact.out
java -jar meteor-1.5.jar left right -norm -m stem > meteor-stem.out
java -jar meteor-1.5.jar left right -norm -m synonym > meteor-synonym.out
java -jar meteor-1.5.jar left right -norm -m paraphrase > meteor-paraphrase.out
grep -Ei '(Segment\s[0-9]*\sscore:)\s*(.*)' meteor-synonym.out | cut -f2 | sed '1,1d' > sts_meteor-synonym.out

# BEER
./beer -l en -s left -r right --norm --printSentScores > beer-norm.out

"""
