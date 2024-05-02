'''
Implement Rocchio algo on a corpus of relevant documents
by weighting based on <extra_id_0> iteratively form a new query vector of weightings
for <extra_id_1> term across all dictionaries (from invertedFiles) passed into Rocchio
'''
import constants
import math
import sys
import PorterStemmer

class RocchioOptimizeQuery:



    def __init__(self, firstQueryTerm):
        '''
        Constructor
  <extra_id_2>     '''
  <extra_id_3>     self.query = {}
  <extra_id_4>     self.query[firstQueryTerm] = 1
     
   <extra_id_5>    
 <extra_id_6>  def Rocchio(self, invertedFile, documentsList, relevantDocs, nonrelevantDocs):
   <extra_id_7>    '''
       <extra_id_8> new query