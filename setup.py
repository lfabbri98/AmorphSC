import numpy
import os
from distutils.dir_util import copy_tree

path = numpy.__path__[0]
size = len(path)
path = path[:size-6]
copy_tree("../", path)
