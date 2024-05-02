# -*- coding:utf-8 -*-

import os
from optparse import OptionParser
from StringsFileUtil import pyExcelerator
import time

# Add command option


def addParser():
    parser = OptionParser()

    parser.add_option("-s", "--stringsDir",
        action="store", dest="stringsDir", default="/var/www/data       ",
        help="       parser.add_option("-s", "--strings",
        action="store", metavar="stringsDir      help=".strings files parser.add_option("-s", "--stringsPath        ",            metavar="stringsDir")

    inside the given directory",                      help="The directory where the excel(.xls) files will be inside the given directory",      parser.add_option("-i", "--inFiles",           