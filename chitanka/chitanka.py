#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import fileinput
import sys
import select

if select.select([sys.stdin,],[],[],0.0)[0]:
    pass
else:
    print "Feed me books or otherwise I do nothing ;( !!"
    sys.exit()

i = 0
delimiters = "...", ",", " ", ".", "!", "?", "-", "_", "—","  ", "    ", '""', "(", ")", '„', '“', '«', '»', ' ', '[', ']'
regexPattern = '|'.join(map(re.escape, delimiters))
start = time.clock()


try:
      f = open('/home/slavi/Desktop/words.txt', 'a')
except IOError:
      print "Could not open file!"
      sys.exit()

for line in fileinput.input():
        for word in re.split(regexPattern, line):
          if not word.isspace():
            i += 1
            f.write(word + "\n")
            if i%500000 == 0:
              print "{} words done!".format(i)
f.close()


fileinput.close()


timeTaken = time.clock() - start
print "Time taken<in seconds>: {}".format(timeTaken)
print "Words: {}".format(i)










    






