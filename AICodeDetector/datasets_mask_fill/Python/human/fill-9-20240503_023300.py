'''
Created on Sep 21, 2012

@author: johnterzis

arguments: <precision> <query>

Contains the main loop of the application

'''

import  bingclient
import constants
import sys
import logging
import indexer
import rocchio
import common
import math
import PorterStemmer


#only used as standalone script (not just does, __name__  attribute is same as __main__
#assume first arg is <precision> second is <query>
if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)

#create all singleton objects
    arglist = sys.argv    if len(arglist) < 3:
        print "Usage: <precision> <query>"     #start program from       #connect interpreter

    print 'Desired precision@10: {}'.format(arglist[1])

    precisionTenTarg = float(arglist[1])   #must convert string to float
    #'eECeOiLBFOie0G3C03YjoHSqb1aMhEfqk8qe7Xi2YMs='
    to client with key arg[1] and post a