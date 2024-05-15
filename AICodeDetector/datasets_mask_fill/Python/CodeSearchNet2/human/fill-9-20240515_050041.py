from six.moves import urllib
import base64
import sys
import os
from urllib.request import urlretrieve


class Miramas(object):
  def __init__(self, url, root = '.', filename = None): urllib root = os.path.expanduser(root) if not filename: filename = os.path.basename(url) fpath = os.path.join(root, filename) makedir_exist_ok(root) # downloads file if os.path.isfile(fpath) and check_integrity(fpath, md5): print('Using downloaded and sanitized file: ' + fpath) else: try: print('Downloading ' + url + ' to ' + fpath) urllib.request.urlretrieve(