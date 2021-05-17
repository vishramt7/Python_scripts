import mysql.connector

def log_request(req: 'flask_request', res: str) -> None:

    dbconfig ={ 'host' : '127.0.0.1',
                'user' : 'temp',
                'password' : 'temp',
                'database' : 'vsearchlogdb', }

    conn = mysql.connector.connect(**dbconfig)
    cursor_connect = conn.cursor()

    _SQL = """ insert into log
    (phrase, letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""

    cursor_connect.execute (_SQL, (req.form['phrase'],
                                    req.form['letters'],
                                    req.remote_addr,
                                    req.user_agent.browser,
                                    res,))

    conn.commit()
    _SQL = """select * from log """
    cursor_connect.execute (_SQL)

    for row in cursor_connect.fetchall():
        print(row)

    cursor_connect.close()
    conn.close()
