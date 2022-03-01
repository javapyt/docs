# Script to index the pages in the folders, author: @Daniel Kwoska 
import os
pathname = os.getcwd()
for subdir, dirs, files in os.walk(pathname):
    print(subdir)
    for file in files:
      for dir in dirs: 
        if(dir + '.md' == file):
          os.rename(subdir + '/' + file, subdir + '/' + dir + '/' + 'index.md')
