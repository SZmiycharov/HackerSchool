import pandas as pd
import psycopg2

data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obl.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obl.csv', encoding='utf-8')



conn = psycopg2.connect("host='' port='5432' dbname='ekatte' user='postgres' password=''")
cur = conn.cursor()

f = open(r'/home/slavi/Desktop/Ek_obl.csv', 'r')
cur.copy_from(f, "oblast", sep=',')
f.close()



conn.commit()
cur.execute('ALTER TABLE oblast DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM oblast WHERE abc = 'abc'")
conn.commit()

conn.close()


