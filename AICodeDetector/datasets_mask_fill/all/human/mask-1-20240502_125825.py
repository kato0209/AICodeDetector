#!/usr/bin/env python

"""Boyer-Moore preprocessing with unittest

Adapted and Enhanced by Jordan Cheah, Oct 2015
Acknowledgement - Original Author: Ben Langmead

"""

import unittest


def z_array(s):
 <extra_id_0>  """ Use Z algorithm (Gusfield theorem 1.4.1) to preprocess s """
    assert len(s) > <extra_id_1>   <extra_id_2> [len(s)] + [0] * (len(s)-1)

    # Initial comparison of <extra_id_3> prefix
    for i <extra_id_4> len(s)):
        if s[i] == <extra_id_5>    <extra_id_6>      z[1] <extra_id_7>        else:
            break

    r, l = 0, 0
  <extra_id_8> if z[1] > 0:
