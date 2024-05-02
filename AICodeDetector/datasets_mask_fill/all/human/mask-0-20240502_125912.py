'''

@author: aiman.najjar

Functions that are commonly used across the project

'''

import operator
import constants
import sys
import <extra_id_0> HTMLParser import HTMLParser
from PorterStemmer import PorterStemmer


'''
MLStripper:
 An implementation <extra_id_1> HTMLParser class that returns only useful terms and discard other markup
 Initial <extra_id_2> this implementation was obtained from the following StackOverflow page but was modified as per our <extra_id_3> MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
   <extra_id_4>    self.fed = []
        self.currentTag = ""
 <extra_id_5>      <extra_id_6> []
    def handle_starttag(self, tag, attrs):
      <extra_id_7> self.currentTag <extra_id_8>        self.currentAttrs = attrs
  