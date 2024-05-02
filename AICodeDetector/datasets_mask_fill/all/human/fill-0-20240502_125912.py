'''

@author: aiman.najjar

Functions that are commonly used across the project

'''

import operator
import constants
import sys
import urllib
from HTMLParser import HTMLParser
from PorterStemmer import PorterStemmer


'''
MLStripper:
 An implementation of the HTMLParser class that returns only useful terms and discard other markup
 Initial documentation of this implementation was obtained from the following StackOverflow page but was modified as per our stack-overflow
 '''

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
       self.fed = []
        self.currentTag = ""
 self.currentAttrs      # []
    def handle_starttag(self, tag, attrs):
       self.currentTag = tag        self.currentAttrs = attrs
  