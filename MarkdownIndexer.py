# Script to index the pages in the folders, author: @Daniel Kwoska 
import os
pathname = os.getcwd()
for subdir, dirs, files in os.walk(pathname):
    for file in files:
      dirname = os.path.dirname(subdir + '/' + file)
      basename = os.path.basename(dirname)
      if basename + '.md' == file:
        os.rename(subdir + '/' + file, subdir + '/' + 'index.md')
