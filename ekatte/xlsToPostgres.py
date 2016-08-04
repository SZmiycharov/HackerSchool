import pandas as pd
import psycopg2

conn = psycopg2.connect("host='' port='5432' dbname='ekatte' user='postgres' password=''")
cur = conn.cursor()

data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obl.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obl.csv', encoding='utf-8')
cur.execute("COPY helperOblasti FROM '/home/slavi/Desktop/Ek_obl.csv' DELIMITER ',' CSV")

data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obst.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obst.csv', encoding='utf-8')
cur.execute("COPY helperObstini FROM '/home/slavi/Desktop/Ek_obst.csv' DELIMITER ',' CSV")

data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_atte.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_atte.csv', encoding='utf-8')
cur.execute("COPY helperSelishta FROM '/home/slavi/Desktop/Ek_atte.csv' DELIMITER ',' CSV")

cur.execute('ALTER TABLE helperSelishta DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM helperSelishta WHERE abc = 'abc'")

cur.execute('ALTER TABLE helperObstini DROP COLUMN "id"')
cur.execute("DELETE FROM helperObstini WHERE abc = 'abc'")

cur.execute('ALTER TABLE helperOblasti DROP COLUMN "id"')
cur.execute("DELETE FROM helperOblasti WHERE abc = 'abc'")

cur.execute('ALTER TABLE helperObstini ADD COLUMN oblast_kod text')
conn.commit()

cur.execute('''UPDATE helperobstini
SET oblast_kod=subquery.oblast_kod
FROM (SELECT oblast_kod, obstina_kod
      FROM helperselishta ) AS subquery
WHERE helperobstini.obstina_kod=subquery.obstina_kod''')
conn.commit()

data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obl.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obl.csv', encoding='utf-8')
cur.execute("COPY oblasti FROM '/home/slavi/Desktop/Ek_obl.csv' DELIMITER ',' CSV")
cur.execute('ALTER TABLE oblasti DROP COLUMN "id"')
cur.execute("DELETE FROM oblasti WHERE abc = 'abc'")
conn.commit()

cur.execute('''INSERT INTO obstini(obstina_kod, ekatte, name, category, document, abc, oblast_kod) 
	SELECT obstina_kod, ekatte, name, category, document, abc, oblast_kod FROM helperobstini''')
cur.execute('''INSERT INTO selishta(ekatte, t_v_m, name, oblast_kod, obstina_kod, kmetstvo_kod, kind, category, altitude, document, tsb, abc) 
	SELECT ekatte, t_v_m, name, oblast_kod, obstina_kod, kmetstvo_kod, kind, category, altitude, document, tsb, abc FROM helperselishta''')
conn.commit()

cur.execute('''DROP TABLE helperSelishta''')
cur.execute('''DROP TABLE helperOblasti''')
cur.execute('''DROP TABLE helperObstini''')
conn.commit()






