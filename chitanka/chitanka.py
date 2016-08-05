#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import fileinput

i = 0
delimiters = "...", ",", " ", ".", "!", "?", "-", "_", "—","  ", "    ", '""', "(", ")", '„', '“', '«', '»', ' ', '[', ']'
regexPattern = '|'.join(map(re.escape, delimiters))
start = time.clock()

print fileinput.input().value

for line in fileinput.input():
  try:
      f = open('/home/slavi/Desktop/words.txt', 'a')
      with f:
        for word in re.split(regexPattern, line):
          if not word.isspace():
            i += 1
            f.write(word + "\n")
            if i%500000 == 0:
              print "{} words done!".format(i)
  except IOError:
      print "Could not open file:"
      sys.exit()
f.close()

timeTaken = time.clock() - start
print "Time taken<in seconds>: {}".format(timeTaken)
print "Words: {}".format(i)










    






