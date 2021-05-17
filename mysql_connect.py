import mysql.connector

dbconfig ={ 'host' : '127.0.0.1',
            'user' : 'temp',
            'password' : 'temp',
            'database' : 'vsearchlogdb', }

conn = mysql.connector.connect(**dbconfig)

cursor_connect = conn.cursor()

#_SQL = """describe log"""
_SQL = """ insert into log
(phrase, letters, ip, browser_string, results)
values
(%s, %s, %s, %s, %s)"""

cursor_connect.execute (_SQL, ('hitch-hiker','xyz','127.0.0.1','Safari','set()'))

conn.commit()
_SQL = """select * from log """
cursor_connect.execute (_SQL)
res = cursor_connect.fetchall()

for row in res:
    print(row)

cursor_connect.close()
conn.close()
