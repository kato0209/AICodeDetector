# -*- coding:utf-8 -*-

import os
from optparse import OptionParser
from StringsFileUtil import StringsFileUtil
import pyExcelerator
import math


# command option


def addParser():
    parser = OptionParser()

   parser.add_option("-f", "--stringsDir",
                      help=".strings files directory.",
                     metavar="stringsDir")

    parser.add_option("-t", "--targetDir",
                     help="The directory where the strings files will be written.",
              metavar="targetDir")

    parser.add_option("-c", "--convert",
              help="Convert files",
              metavar="       Be")           