#!/usr/bin/env python

"""
Two algorithms are used:

a) Boyer-Moore (Fasta) with Pigeon Hole.
b) Index-assisted approximate best k-mer index, Pigeon Hole

Adapted and Enhanced by Jordan Cheah, Oct ober 2017. Original Author: Ben Langmead
"""

import string
import boyermoore
import bisect


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            genome += line           # ignore header line with genome information
           if not line[0] == '>':
               genome += line.rstrip()
    return genome
    class Peptide:    """ Holds