import pandas as pd
import psycopg2

conn = psycopg2.connect("host='' port='5432' dbname='ekatte' user='postgres' password=''")
cur = conn.cursor()


data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obl.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obl.csv', encoding='utf-8')
f = open(r'/home/slavi/Desktop/Ek_obl.csv', 'r')
cur.copy_from(f, "oblast", sep=',')
f.close()
conn.commit()
cur.execute('ALTER TABLE oblast DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM oblast WHERE abc = 'abc'")
conn.commit()


data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obst.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obst.csv', encoding='utf-8')
f = open(r'/home/slavi/Desktop/Ek_obst.csv', 'r')
cur.copy_from(f, "obstina", sep=',')
f.close()
conn.commit()
cur.execute('ALTER TABLE obstina DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM obstina WHERE abc = 'abc'")
conn.commit()


data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_kmet.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_kmet.csv', encoding='utf-8')
f = open(r'/home/slavi/Desktop/Ek_kmet.csv', 'r')
cur.copy_from(f, "kmetstvo", sep=',')
f.close()
conn.commit()
cur.execute('ALTER TABLE kmetstvo DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM kmetstvo WHERE document = 'document'")
conn.commit()




#WORKS FINE BEFORE HERE!!! ************************************************************************************************




data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_sobr.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_sobr.csv', encoding='utf-8')
f = open(r'/home/slavi/Desktop/Ek_sobr.csv', 'r')
cur.copy_from(f, "obrazuvanie", sep=',')
f.close()
conn.commit()
cur.execute('ALTER TABLE obrazuvanie DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM obrazuvanie WHERE abc = 'document'")
conn.commit()


