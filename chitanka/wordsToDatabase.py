#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import time
import sys

conn = psycopg2.connect("host='' port='5432' dbname='chitanka' user='postgres' password=''")
cur = conn.cursor()

iterator = 0

try:
	with open('/home/slavi/Desktop/words.txt', 'r') as f:
		startMain = time.clock()
		startInner = time.clock()
		for line in f:
			iterator += 1
			if iterator%200000 == 0:
				timeTakenFor200000words = time.clock() - startInner

				print "{} words iterated!".format(iterator)
				print "Time taken for 200k words: {} seconds".format(timeTakenFor200000words)

				startInner = time.clock()
			try:
				if not line.isspace() and not line.isdigit():
					word = line.split('\n')[0].decode('utf-8').lower()
					query = "INSERT INTO dictionary VALUES ('%s')"%(word)
					cur.execute(query)
					conn.commit()
			except:
				conn.commit()
				pass
		timeTaken = time.clock() - startMain
		print "Total time taken: {} seconds".format(timeTaken)
except IOError:
	print "Could not open file!"
	sys.exit()

cur.execute("SELECT count(*) FROM dictionary")
WordsInBGLanguage = cur.fetchone()
WordsInBGLanguage = WordsInBGLanguage[0]
print "According to my dictionary, WordsInBGLanguage are: {}".format(WordsInBGLanguage)