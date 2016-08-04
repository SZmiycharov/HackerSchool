import psycopg2

conn = psycopg2.connect("host='' port='5432' dbname='chitanka' user='postgres' password=''")
cur = conn.cursor()

query = "INSERT INTO dictionary SELECT \'" + word + "\' WHERE NOT EXISTS (SELECT * FROM dictionary WHERE words = \'" + word + "\')"
                       cur.execute(query)
                       conn.commit()

                       
cur.execute("SELECT count(*) FROM dictionary")
WordsInBGLanguage = cur.fetchone()
WordsInBGLanguage = WordsInBGLanguage[0]
print "According to my dictionary, WordsInBGLanguage are: {}".format(WordsInBGLanguage)