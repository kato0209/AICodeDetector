'''
Created on Sep 21, 2012

@author: johnterzis

arguments: <precision> <query>

Contains the main loop of the application

'''

import <extra_id_0> bingclient
import constants
import <extra_id_1> logging
import indexer
import rocchio
import common
import math
import PorterStemmer


#only <extra_id_2> as standalone script (not <extra_id_3> does, __name__  attribute <extra_id_4> __main__
#assume first arg is <precision> second is <query>
if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)

#create all singleton objects
    arglist <extra_id_5>    if len(arglist) < 3:
        print "Usage: <precision> <extra_id_6>       <extra_id_7> interpreter

    print 'Desired precision@10: {}'.format(arglist[1])

    precisionTenTarg = float(arglist[1])   #must convert string to float
    #'eECeOiLBFOie0G3C03YjoHSqb1aMhEfqk8qe7Xi2YMs='
   <extra_id_8> to client with key arg[1] and post a