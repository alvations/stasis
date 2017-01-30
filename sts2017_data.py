#!/usr/bin/env python3 -*- coding: utf-8 -*-

import io
import os
import re
from unicodedata import normalize

def clean(text):
    text = text.replace(u"�", "e").replace(u'”', '"').replace(u'“', '')
    text = text.replace(u"\x92", "'").replace(u"\x91", "").replace(u"\x93", "").replace(u"\x94", "").replace(u"\x95", "")
    text = text.replace(u"‚Äôs", "'s").replace(u"Äė", "").replace(u"‚Äė", "").replace(u"‚Äô", "").replace(u"‚Äď", "").replace(u"‚ā¨", "").replace(u"‚ÄĒ", "")
    text = text.replace(u"😢🐶", "")
    return text

#line = normalize('NFKD', line).encode('ascii', 'ignore')

sts2017 = {'STS2017-test/STS.input.track1.ar-ar.txt': 'STS2017-test-translated/STS2017.track1.ar-ar',
           'STS2017-test/STS.input.track2.ar-en.txt': 'STS2017-test-translated/STS2017.track2.ar-en',
           'STS2017-test/STS.input.track3.es-es.txt': 'STS2017-test-translated/STS2017.track3.es-es',
           'STS2017-test/STS.input.track4a.es-en.txt': 'STS2017-test-translated/STS2017.track4a.es-en',
           'STS2017-test/STS.input.track4b.es-en.txt': 'STS2017-test-translated/STS2017.track4b.es-en',
           'STS2017-test/STS.input.track5.en-en.txt': 'STS2017-test-translated/STS2017.track5.en-en',
           'STS2017-test/STS.input.track6.tr-en.txt': 'STS2017-test-translated/STS2017.track6.tr-en'
           }


def create_allinone_csv_file():
    fout = io.open('sts2017.csv', 'w')
    headerline = "\t".join(['Dataset', 'Domain', 'Sent1', 'Sent2', 'Sent1_original', 'Sent2_original'])
    fout.write(unicode(headerline)+'\n')
    dataset = 'STS2017'
    for originalfile, translationfile in sorted(sts2017.items()):
        domain = translationfile.partition('.')[2]
        with io.open('STS-data/'+originalfile, 'r', encoding='utf8') as orifin:
            with io.open('STS-data/'+translationfile, 'r', encoding='utf8') as transfin:
                for original, translation in zip(orifin, transfin):
                    translation = normalize('NFKD', translation).encode('ascii', 'ignore')
                    sent1_original, sent2_original = original.strip().split('\t')
                    sent1_translation, sent2_translation = translation.strip().split('\t')
                    outline = '\t'.join([dataset, domain, sent1_translation, sent2_translation, sent1_original, sent2_original])
                    fout.write(unicode(outline)+'\n')

create_allinone_csv_file()
