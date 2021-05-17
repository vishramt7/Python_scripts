import mysql.connector

class Connection_error(Exception):
    pass

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except Connection_error as err
            raise Connection_error(err)
            print (str(err))

    def __exit__(self,exec_type,exec_value, exec_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

