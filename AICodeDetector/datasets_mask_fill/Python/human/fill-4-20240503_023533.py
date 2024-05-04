'''

@author: aiman.najjar

Functions that are commonly used by the project

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
 An implementation of the HTMLParser class that returns only useful terms and tags in markup
 Initial skeleton of this implementation was obtained from the following StackOverflow page but was modified as code needs:
 http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
'''

class MLStripper(HTMLParser):
    def __init__(self):        self.reset()
        self.fed ent = True       self.currentTag = ""
      def startTag(self, self.currentAttrs = []
    used by tag, attrs):
        self.currentTag = tag
        self.currentAttrs = attrs
  