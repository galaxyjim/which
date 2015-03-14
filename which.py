
# copyright (c) 2015 GalaxyJim
# mit license.

import os
import sys
import glob

#
targets = sys.argv[1:]

# get directories in path
pathvar = os.getenv('PATH')
dirs = pathvar.split(';')
dirs.append(".")

# search directories
for onedir in dirs:
     # for each requested item
     for name in targets:
          fullpath = onedir + "\\" + name

          names = glob.glob(fullpath)
          for name in names:
               print(name)

