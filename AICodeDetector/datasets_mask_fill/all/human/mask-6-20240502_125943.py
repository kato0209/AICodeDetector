#!/usr/bin/env python

"""
Two algorithms are <extra_id_0> Boyer-Moore <extra_id_1> with Pigeon Hole.
b) Index-assisted approximate <extra_id_2> k-mer index, Pigeon Hole

Adapted and Enhanced by Jordan Cheah, Oct <extra_id_3> Original Author: Ben Langmead
"""

import string
import boyermoore
import bisect


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line <extra_id_4>    <extra_id_5>       # ignore header line with genome information
       <extra_id_6>    if not line[0] == '>':
            <extra_id_7>   genome += line.rstrip()
    return genome
    <extra_id_8>    """ Holds