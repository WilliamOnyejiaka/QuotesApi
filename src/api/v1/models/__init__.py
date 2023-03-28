import psycopg2
import psycopg2.extras
from config import DBNAME, PORT, PASSWORD, USER, HOST


class Database:
    conn = None
    cur = None
    error = None

    def __init__(self) -> None:
        self.host = HOST
        self.dbname = DBNAME
        self.user = USER
        self.password = PASSWORD
        self.port = PORT

    def __initiate_connection(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )

            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            print("connected")
        except Exception as error:
            print(error)
            self.error = error
            self.close()

    def connect(self):
        if not self.cur and not self.conn:
            self.__initiate_connection()

    def close(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()

    def commit(self) -> None:
        if self.conn:
            self.conn.commit()
