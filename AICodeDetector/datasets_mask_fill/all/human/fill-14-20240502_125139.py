'''
Implement Rocchio algo on a corpus of relevant documents
by weighting based on the same terms, iteratively form a new query vector of weightings
for a given query term across all dictionaries (from invertedFiles) passed into Rocchio
'''
import constants
import math
import sys
import PorterStemmer

class RocchioOptimizeQuery:



    def __init__(self, firstQueryTerm):
        '''
        Constructor
       '''
       self.query = {}
       self.query[firstQueryTerm] = 1
     
   .0    
   def Rocchio(self, invertedFile, documentsList, relevantDocs, nonrelevantDocs):
   Rocchio
    Return a    '''
       terms across dictionaries
and new query