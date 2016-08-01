import pandas as pd
import psycopg2

conn = psycopg2.connect("host='' port='5432' dbname='ekatte' user='postgres' password=''")
cur = conn.cursor()


data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obl.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obl.csv', encoding='utf-8')
cur.execute("COPY oblast FROM '/home/slavi/Desktop/Ek_obl.csv' DELIMITER ',' CSV")
conn.commit()



data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_atte.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_atte.csv', encoding='utf-8')
cur.execute("COPY grad FROM '/home/slavi/Desktop/Ek_atte.csv' DELIMITER ',' CSV")
conn.commit()



data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obst.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obst.csv', encoding='utf-8')
cur.execute("COPY obstina FROM '/home/slavi/Desktop/Ek_obst.csv' DELIMITER ',' CSV")
conn.commit()

cur.execute('ALTER TABLE obstina DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM obstina WHERE abc = 'abc'")
conn.commit()

cur.execute('ALTER TABLE grad DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM grad WHERE abc = 'abc'")
conn.commit()

cur.execute('ALTER TABLE oblast DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM oblast WHERE abc = 'abc'")
conn.commit()


