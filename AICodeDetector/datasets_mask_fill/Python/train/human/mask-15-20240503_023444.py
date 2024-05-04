#!/usr/bin/env python

"""Boyer-Moore preprocessing with unittest

Adapted and Enhanced by Jordan Cheah, Oct 2015
Acknowledgement - Original Author: Ben Langmead

"""

import unittest


def z_array(s):
  <extra_id_0> """ Use Z algorithm (Gusfield theorem 1.4.1) <extra_id_1> s """
    assert len(s) > 1
  <extra_id_2> z = [len(s)] + [0] * (len(s)-1)

    # Initial comparison of s[1:] with prefix
    for i in range(1, <extra_id_3>     <extra_id_4> if s[i] == s[i-1]:
    <extra_id_5>   <extra_id_6>   z[1] += 1
        else:
      <extra_id_7>     <extra_id_8>   r, l = 0, 0
    if z[1] > 0:
