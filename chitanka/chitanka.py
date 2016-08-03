#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psycopg2
import re

conn = psycopg2.connect("host='' port='5432' dbname='chitanka' user='postgres' password=''")
cur = conn.cursor()

i = 0

for filename in os.listdir("/home/slavi/Desktop/books"):
    if filename.endswith(".txt"):
        with open("/home/slavi/Desktop/books/" + filename, 'r') as f:
            lines = f.read()
            for split0 in lines.split(' '):
                for split1 in split0.split(','):
                    for split2 in split1.split('.'):
                        for split3 in split2.split('?'):
                            for split4 in split3.split('!'):
                                for split5 in split4.split(':'):
                                    for split6 in split5.split('...'):
                                        for word in split6.split(): 
                                            if word != "" and word != "-" and word != "\r\n":
                                                print(word.decode('utf-8').lower())
                                                word = word.decode('utf-8').lower()
                                                query = "INSERT INTO dictionary SELECT \'" + word + "\' WHERE NOT EXISTS (SELECT * FROM dictionary WHERE words = \'" + word + "\')"
                                                cur.execute(query)
                                                conn.commit()
cur.execute("SELECT count(*) FROM dictionary")
WordsInBGLanguage = cur.fetchone()
WordsInBGLanguage = WordsInBGLanguage[0]
print "According to my dictionary, WordsInBGLanguage are: {}".format(WordsInBGLanguage)


                




