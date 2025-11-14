#!/usr/bin/env python3
import pymysql.cursors
from random import randint
try:
    # Verbindungsaufbau
    conn = pymysql.connect(host='localhost',
                           user='pyuser',
                           password='geheim',
                           db='pytest',
                           charset='utf8mb4',
                           cursorclass=\
                             pymysql.cursors.DictCursor)
    
    # Datensatz speichern
    with conn.cursor() as cur:
       sql = 'INSERT INTO mytable(txt, nmb) VALUES(%s, %s)'
       cur.execute(sql, ('abc äöü', randint(0, 1000)))
       conn.commit()
       print('ID des neuen Datensatzes:', cur.lastrowid)

    # alle Datensätze abfragen
    with conn.cursor() as cur:
       sql = 'SELECT * FROM mytable'
       cur.execute(sql)
       result = cur.fetchone()
       while result:
           print('ID=%d txt=%s nmb=%d' % 
             (result['id'], result['txt'], result['nmb']))
           result = cur.fetchone()

except BaseException as ex:
    print('Fehler:', ex)
finally:
    if 'conn' in locals() and conn:
        conn.close()
