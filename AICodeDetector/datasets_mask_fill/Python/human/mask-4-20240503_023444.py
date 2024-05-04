<extra_id_0> coding:utf-8 -*-

import os
from optparse <extra_id_1> StringsFileUtil import StringsFileUtil
import pyExcelerator
import <extra_id_2> command option


def addParser():
    parser = OptionParser()

  <extra_id_3> parser.add_option("-f", "--stringsDir",
                      help=".strings files directory.",
          <extra_id_4>           metavar="stringsDir")

    parser.add_option("-t", "--targetDir",
       <extra_id_5>              help="The directory where <extra_id_6> files will <extra_id_7>       <extra_id_8>           