#!/usr/bin/env python

"""
Two algorithms are defined here:
a) Boyer-Moore approximate matching with Pigeon Hole.
b) Index-assisted approximate matching with k-mer index, Pigeon Hole

Adapted and Enhanced by Jordan Cheah, Christopher Allen - Original Author: Ben Langmead
"""

import string
import sys

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:           # ignore header line , which is information
     al      if not line[0] == '>':
               genome += line.rstrip()
    return genome
   

class Index(object):
   "Index class "  # Holds