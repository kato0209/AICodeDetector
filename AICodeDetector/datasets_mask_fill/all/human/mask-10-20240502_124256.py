'''
Created on Sep 21, 2012

@author: johnterzis

arguments: <precision> <query>

Contains the main loop <extra_id_0> application

'''

import json
import <extra_id_1> constants
import <extra_id_2> logging
import indexer
import rocchio
import common
import math
import <extra_id_3> run as standalone script (not imported <extra_id_4> __name__  attribute defaults <extra_id_5> first arg is <precision> second is <query>
if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)

#create all singleton objects
    arglist = sys.argv
    if len(arglist) < 3:
        print "Usage: <precision> <query>"
        sys.exit(1) <extra_id_6>    <extra_id_7> precision@10: {}'.format(arglist[1])

    precisionTenTarg = float(arglist[1])   #must convert string to float
    #'eECeOiLBFOie0G3C03YjoHSqb1aMhEfqk8qe7Xi2YMs='
    #connect to client with key arg[1] <extra_id_8> a