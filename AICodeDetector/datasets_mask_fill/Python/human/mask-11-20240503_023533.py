#!/usr/bin/env python
'''
Generic Naive Approximate Matching which allows <extra_id_0> and Enhanced by Jordan Cheah, Oct 2015
Acknowledgement - Original Author: Ben Langmead
'''

import string
  
def naive(p, t):
    occurrences = <extra_id_1>   for i in range(len(t) - <extra_id_2> 1):
 <extra_id_3>  <extra_id_4>   match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
    <extra_id_5>           match <extra_id_6>     <extra_id_7>          break
    <extra_id_8>   if match:
      