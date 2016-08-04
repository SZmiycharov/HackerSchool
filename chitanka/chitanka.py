#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time


words = raw_input()


delimiters = "...", ",", " ", ".", "!", "?", "-"
regexPattern = '|'.join(map(re.escape, delimiters))



try:
    f = open('/home/slavi/Desktop/HackerSchool/chitanka/words.txt', 'w')
except IOError:
    print "Could not open file:"
    sys.exit()

with f:
  for word in re.split(regexPattern, words):
    f.write(word + "\n")
    






