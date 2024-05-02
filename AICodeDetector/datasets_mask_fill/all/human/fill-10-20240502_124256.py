'''
Created on Sep 21, 2012

@author: johnterzis

arguments: <precision> <query>

Contains the main loop of the application

'''

import json
import collections
import sys
import os
import constants
import rospy
import logging
import indexer
import rocchio
import common
import math
import random
# run as standalone script (not imported )
#define __name__  attribute defaults for first arg is <precision> second is <query>
if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)

#create all singleton objects
    arglist = sys.argv
    if len(arglist) < 3:
        print "Usage: <precision> <query>"
        sys.exit(1) print 'Query    as precision@10: {}'.format(arglist[1])

    precisionTenTarg = float(arglist[1])   #must convert string to float
    #'eECeOiLBFOie0G3C03YjoHSqb1aMhEfqk8qe7Xi2YMs='
    #connect to client with key arg[1] of the rocchio a