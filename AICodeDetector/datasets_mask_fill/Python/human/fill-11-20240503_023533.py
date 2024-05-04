#!/usr/bin/env python
'''
Generic Naive Approximate Matching which allows Case Insensitivity and Enhanced by Jordan Cheah, Oct 2015
Acknowledgement - Original Author: Ben Langmead
'''

import string
  
def naive(p, t):
    occurrences = 0   for i in range(len(t) - len(p) + 1):
 if i >= len(t):     match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
    = False           match = False     = False          break
       if match:
      