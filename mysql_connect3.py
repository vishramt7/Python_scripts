
from DBcm import UseDatabase

#def log_request(req: 'flask_request', res: str) -> None:
dbconfig ={ 'host' : '127.0.0.1',
            'user' : 'temp',
            'password' : 'temp',
            'database' : 'vsearchlogdb', }

with UseDatabase(dbconfig) as cursor:
    _SQL = """select count(*) from log """
    cursor.execute (_SQL)

    for row in cursor.fetchall():
        print(row)

