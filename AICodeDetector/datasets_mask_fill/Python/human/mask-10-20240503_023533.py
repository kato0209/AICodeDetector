#!/usr/bin/env python

"""
Two algorithms <extra_id_0> here:
a) Boyer-Moore approximate matching with Pigeon Hole.
b) Index-assisted approximate matching with k-mer index, Pigeon Hole

Adapted and Enhanced by Jordan Cheah, <extra_id_1> - Original Author: Ben Langmead
"""

import string
import <extra_id_2> readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in <extra_id_3>           # ignore header line <extra_id_4> information
     <extra_id_5>      if not line[0] == '>':
            <extra_id_6>   genome += line.rstrip()
    return genome
  <extra_id_7> 

class Index(object):
   <extra_id_8> Holds