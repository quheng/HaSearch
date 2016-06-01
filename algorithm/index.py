import cPickle
import os
import gzip
_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
_FILE_PATH = os.path.join(_FILE_PATH, 'inverse_index.p')
# index = cPickle.load(gzip.open(_FILE_PATH, "rb"))
index = cPickle.load(open(_FILE_PATH, "rb"))
