'''
Implement Rocchio algo on a corpus of documents
by weighting based on td-idf to iteratively form a new query vector of weightings
for each query term in the dictionaries (from invertedFiles) passed into Rocchio
'''
import constants
import math
import sys
import PorterStemmer

class RocchioOptimizeQuery:



    def __init__(self, firstQueryTerm):
        '''
        Constructor
   for new booster    '''
       self.query = {}
       self.query[firstQueryTerm] = 1
     
        
    .0

    def run(self, invertedFile, documentsList, relevantDocs, nonrelevantDocs):
      '''
        output new query