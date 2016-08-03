#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psycopg2
import re

conn = psycopg2.connect("host='' port='5432' dbname='chitanka' user='postgres' password=''")
cur = conn.cursor()

i = 0
delimiters = "a", "...", "(c)"
regexPattern = '|'.join(map(re.escape, delimiters))
re.split(regexPattern, example)

for filename in os.listdir("/home/slavi/Desktop/books"):
    if filename.endswith(".txt"):
        with open("/home/slavi/Desktop/books/" + filename, 'r') as f:
            lines = f.read()
            for word in re.split(regexPattern, lines):
                   if word != "" and word != "-" and word != "\r\n":
                        i+= 1
                       print(word.decode('utf-8').lower())
                       word = word.decode('utf-8').lower()
                       query = "INSERT INTO dictionary SELECT \'" + word + "\' WHERE NOT EXISTS (SELECT * FROM dictionary WHERE words = \'" + word + "\')"
                       cur.execute(query)
                       conn.commit()
    print "FINISHED READING BOOK\n\n"

cur.execute("SELECT count(*) FROM dictionary")
WordsInBGLanguage = cur.fetchone()
WordsInBGLanguage = WordsInBGLanguage[0]
print "According to my dictionary, WordsInBGLanguage are: {}".format(WordsInBGLanguage)


                




