## Stasis - Python wrapper for Semantic Similarity datasets

Under the auspice of the EXPERT project (http://expert-itn.eu/), we have written a python wrapper to the STS datasets and we hope that it helps anyone with easy manipulation the datasets. 

If you just need a tab-separated file, you can easily find the `sts.csv` available in the same repository. The repo also contains other (maybe) useful datasets that are manually compiled by the maintainer when they are free. 

**Disclaimer**: The repository comes as it is. It should **NOT** be considered as the official SemEval's (Semantic Textual Similarity) STS data and it is not affiliated with the STS organizers. We've created this so that people can easily do something like `pandas.read_csv('sts.csv')`  or `graphlab.SFrame('sts.csv')` and work with the dataframes with little hassle.

## Datasets

Below is a list of datasets/wrappers you can find here

 - **STS**: [SemEval Semantic Textual Similarity](http://alt.qcri.org/semeval2016/task1/) (STS2012 - 2015)
 - **CLSS**: [SemEval Cross-level Semantic Similarity](http://alt.qcri.org/semeval2014/task3/) (CLSS)
 - **SICK**: [Sentences Involving Compositional Knowledge](http://www.lrec-conf.org/proceedings/lrec2014/pdf/363_Paper.pdf) 
 
## Contribute

Please feel free to add datasets/wrappers to the repository. Or post an issue to request for wrappers to the repository. 


## Cite

**Please cite the respective references for the datasets when using them in your publication!** 

If you want to cite this repository, you can cite [this paper](http://www.aclweb.org/anthology/S15-2015) where we created used the `sts.csv` in SemEval-2015 
