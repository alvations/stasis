echo """input=raw

#SOURCE definition ==================================
src=right
#REFERENCE definition ==================================
ref=right
#SYSTEM OUTPUT definition ==============================
sys=left
#-------------------------------------------------------


srclang=en
srccase=en
trglang=en
trgcase=en

all_meteor= METEOR-ex METEOR-st METEOR-sy METEOR-pa Ol

all_ngram= NGRAM-cosChar2ngrams NGRAM-cosChar3ngrams NGRAM-cosChar4ngrams NGRAM-cosChar5ngrams NGRAM-cosTok2ngrams NGRAM-cosTok3ngrams NGRAM-cosTok4ngrams NGRAM-cosTok5n$

all_algn= ALGNp ALGNr ALGNs

all_SP= SP-Oc(*) SP-Oc(ADJP) SP-Oc(ADVP) SP-Oc(CONJP) SP-Oc(INTJ) SP-Oc(LST) SP-Oc(NP) SP-Oc(O) SP-Oc(PP) SP-Oc(PRT) SP-Oc(SBAR) SP-Oc(UCP) SP-Oc(VP) SP-cNIST SP-cNIST-1$

all_DP= DP-HWCM_c-1 DP-HWCM_c-2 DP-HWCM_c-3 DP-HWCM_c-4 DP-HWCM_r-1 DP-HWCM_r-2 DP-HWCM_r-3 DP-HWCM_r-4 DP-HWCM_w-1 DP-HWCM_w-2 DP-HWCM_w-3 DP-HWCM_w-4 DP-HWCMi_c-2 DP-H$

all_CP= CP-Oc(*) CP-Oc(ADJP) CP-Oc(ADVP) CP-Oc(CONJP) CP-Oc(FRAG) CP-Oc(INTJ) CP-Oc(LST) CP-Oc(NAC) CP-Oc(NP) CP-Oc(NX) CP-Oc(O) CP-Oc(PP) CP-Oc(PRN) CP-Oc(PRT) CP-Oc(QP$

all_NE= NE-Me(*) NE-Me(ANGLE_QUANTITY) NE-Me(DATE) NE-Me(DISTANCE_QUANTITY) NE-Me(LANGUAGE) NE-Me(LOC) NE-Me(MEASURE) NE-Me(METHOD) NE-Me(MISC) NE-Me(MONEY) NE-Me(NUM) N$

all_ESA= ESA-en

all_SR= SR-Fr(*) SR-MFr(*) SR-MPr(*) SR-MRr(*) SR-Mr(*) SR-Mr(*)_b SR-Mr(*)_i SR-Mr(A0) SR-Mr(A1) SR-Mr(A2) SR-Mr(A3) SR-Mr(A4) SR-Mr(A5) SR-Mr(AA) SR-Mr(AM-ADV) SR-Mr(A$

all_DR= DR-Fr(*) DR-Frp(*) DR-Ol DR-Or(*) DR-Or(*)_b DR-Or(*)_i DR-Or(alfa) DR-Or(card) DR-Or(drs) DR-Or(eq) DR-Or(imp) DR-Or(merge) DR-Or(named) DR-Or(not) DR-Or(or) DR$
""" > assiya.config


nohup $ASIYA_HOME/bin/Asiya.pl -eval single -g seg -m NGRAM-cosChar2ngrams,NGRAM-cosChar3ngrams,NGRAM-cosChar4ngrams,NGRAM-cosChar5ngrams,NGRAM-cosTok2ngrams,NGRAM-cosTok3ngrams,NGRAM-cosTok4ngrams,NGRAM-cosTok5ngrams,NGRAM-jacChar2ngrams,NGRAM-jacChar3ngrams,NGRAM-jacChar4ngrams,NGRAM-jacChar5ngrams,NGRAM-jacCognates,NGRAM-jacTok2ngrams,NGRAM-jacTok3ngrams,NGRAM-jacTok4ngrams,NGRAM-jacTok5ngrams,NGRAM-lenratio assiya.config | sed '2d' | sed 's/ \+ /\t/g' | cut -f 3- > ass.ngram.out &

nohup $ASIYA_HOME/bin/Asiya.pl -eval single -g seg -m "SP-Oc(*),SP-Oc(ADJP),SP-Oc(ADVP),SP-Oc(CONJP),SP-Oc(INTJ),SP-Oc(LST),SP-Oc(NP),SP-Oc(O),SP-Oc(PP),SP-Oc(PRT),SP-Oc(SBAR),SP-Oc(UCP),SP-Oc(VP),SP-cNIST,SP-cNIST-1,SP-cNIST-2,SP-cNIST-3,SP-cNIST-4,SP-cNIST-5,SP-cNISTi-2,SP-cNISTi-3,SP-cNISTi-4,SP-cNISTi-5,SP-iobNIST,SP-iobNIST-1,SP-iobNIST-2,SP-iobNIST-3,SP-iobNIST-4,SP-iobNIST-5,SP-iobNISTi-2,SP-iobNISTi-3,SP-iobNISTi-4,SP-iobNISTi-5,SP-lNIST,SP-lNIST-1,SP-lNIST-2,SP-lNIST-3,SP-lNIST-4,SP-lNIST-5,SP-lNISTi-2,SP-lNISTi-3,SP-lNISTi-4,SP-lNISTi-5,SP-pNIST,SP-pNIST-1,SP-pNIST-2,SP-pNIST-3,SP-pNIST-4,SP-pNIST-5,SP-pNISTi-2,SP-pNISTi-3,SP-pNISTi-4,SP-pNISTi-5" assiya.config | sed '2d' | sed 's/ \+ /\t/g' | cut -f 3- > ass.sp.out &

nohup $ASIYA_HOME/bin/Asiya.pl -eval single -g seg -m "NE-Me(*),NE-Me(ANGLE_QUANTITY),NE-Me(DATE),NE-Me(DISTANCE_QUANTITY),NE-Me(LANGUAGE),NE-Me(LOC),NE-Me(MEASURE),NE-Me(METHOD),NE-Me(MISC),NE-Me(MONEY),NE-Me(NUM),NE-Me(ORG),NE-Me(PER),NE-Me(PERCENT),NE-Me(PROJECT),NE-Me(SIZE_QUANTITY),NE-Me(SPEED_QUANTITY),NE-Me(SYSTEM),NE-Me(TEMPERATURE_QUANTITY),NE-Me(TIME),NE-Me(WEIGHT_QUANTITY),NE-Oe(*),NE-Oe(**),NE-Oe(ANGLE_QUANTITY),NE-Oe(DATE),NE-Oe(DISTANCE_QUANTITY),NE-Oe(LANGUAGE),NE-Oe(LOC),NE-Oe(MEASURE),NE-Oe(METHOD),NE-Oe(MISC),NE-Oe(MONEY),NE-Oe(NUM),NE-Oe(O),NE-Oe(ORG),NE-Oe(PER),NE-Oe(PERCENT),NE-Oe(PROJECT),NE-Oe(SIZE_QUANTITY),NE-Oe(SPEED_QUANTITY),NE-Oe(SYSTEM),NE-Oe(TEMPERATURE_QUANTITY),NE-Oe(TIME),NE-Oe(WEIGHT_QUANTITY)" assiya.config | sed '2d' | sed 's/ \+ /\t/g' | cut -f 3- > ass.ne.out &

java -jar meteor-1.5.jar left right -norm | awk 'NR > 11 { print }' | cut -f2

./beer -l en -s left -r right --norm --printSentScores | sed 's/ \+/\t/g' | cut -f4 > beer-norm.out

'

 nohup python takelab_simple_features.py left-right > takelab-feats.txt 2> takelabfeat.log &
 nohup python takelab_simple_features.py test.txt > test.takelab-feats.txt 2> test.takelabfeat.log &
 
 cat takelab-feats.txt | s/^0.0 //;s/[0-9]\+:\([0-9.]\+\)/\1/g' 
 cat test.takelab-feats.txt | s/^0.0 //;s/[0-9]\+:\([0-9.]\+\)/\1/g' 
