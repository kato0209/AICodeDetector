'''

@author: aiman.najjar

Functions that are commonly <extra_id_0> the project

'''

import operator
import constants
import sys
import logging
import re
from HTMLParser import HTMLParser
from PorterStemmer import PorterStemmer


'''
MLStripper:
 An implementation of the HTMLParser class that returns only useful terms and <extra_id_1> markup
 Initial skeleton of this implementation was obtained <extra_id_2> following StackOverflow page but was modified as <extra_id_3> needs:
 http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
'''

class MLStripper(HTMLParser):
    <extra_id_4>        self.reset()
        self.fed <extra_id_5>      <extra_id_6> self.currentTag = ""
      <extra_id_7> self.currentAttrs = []
    <extra_id_8> tag, attrs):
        self.currentTag = tag
        self.currentAttrs = attrs
  