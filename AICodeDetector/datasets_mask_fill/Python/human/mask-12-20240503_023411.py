'''
Implement Rocchio algo on a corpus <extra_id_0> documents
by weighting based on td-idf to iteratively form a new query vector of weightings
for <extra_id_1> term <extra_id_2> dictionaries (from invertedFiles) passed into Rocchio
'''
import constants
import math
import sys
import PorterStemmer

class RocchioOptimizeQuery:



    def __init__(self, firstQueryTerm):
        '''
        Constructor
   <extra_id_3>    '''
 <extra_id_4>      self.query = {}
     <extra_id_5>  self.query[firstQueryTerm] = 1
     
        
    <extra_id_6> invertedFile, documentsList, relevantDocs, nonrelevantDocs):
  <extra_id_7>   <extra_id_8> '''
        output new query