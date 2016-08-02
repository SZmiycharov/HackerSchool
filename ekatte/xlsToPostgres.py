import pandas as pd
import psycopg2

conn = psycopg2.connect("host='' port='5432' dbname='ekatte' user='postgres' password=''")
cur = conn.cursor()



data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obl.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obl.csv', encoding='utf-8')
cur.execute("COPY helperOblast FROM '/home/slavi/Desktop/Ek_obl.csv' DELIMITER ',' CSV")
conn.commit()


data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obst.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obst.csv', encoding='utf-8')
cur.execute("COPY helperObstina FROM '/home/slavi/Desktop/Ek_obst.csv' DELIMITER ',' CSV")
conn.commit()


data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_atte.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_atte.csv', encoding='utf-8')
cur.execute("COPY helperSelishte FROM '/home/slavi/Desktop/Ek_atte.csv' DELIMITER ',' CSV")
conn.commit()


cur.execute('ALTER TABLE helperSelishte DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM helperSelishte WHERE abc = 'abc'")
conn.commit()


cur.execute('ALTER TABLE helperObstina DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM helperObstina WHERE abc = 'abc'")
conn.commit()

cur.execute('ALTER TABLE helperOblast DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM helperOblast WHERE abc = 'abc'")
conn.commit()

cur.execute('ALTER TABLE public.helperobstina ADD COLUMN oblast text')
conn.commit()

cur.execute('''UPDATE helperobstina
SET oblast=subquery.oblast
FROM (SELECT oblast, obstina
      FROM helperselishte ) AS subquery
WHERE helperobstina.obstina=subquery.obstina''')
conn.commit()

data_xls = pd.read_excel('/home/slavi/Desktop/ekatte/important/Ek_obl.xls', index_col=None)
data_xls.to_csv('/home/slavi/Desktop/Ek_obl.csv', encoding='utf-8')
cur.execute("COPY oblast FROM '/home/slavi/Desktop/Ek_obl.csv' DELIMITER ',' CSV")
conn.commit()
cur.execute('ALTER TABLE oblast DROP COLUMN "id"')
conn.commit()
cur.execute("DELETE FROM oblast WHERE abc = 'abc'")
conn.commit()

cur.execute('''INSERT INTO obstina(obstina, ekatte, name, category, document, abc, oblast) 
	SELECT obstina, ekatte, name, category, document, abc, oblast FROM helperobstina''')
conn.commit()

cur.execute('''INSERT INTO selishte(ekatte, t_v_m, name, oblast, obstina, kmetstvo, kind, category, altitude, document, tsb, abc) 
	SELECT ekatte, t_v_m, name, oblast, obstina, kmetstvo, kind, category, altitude, document, tsb, abc FROM helperselishte''')
conn.commit()






