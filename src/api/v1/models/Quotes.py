from typing import Tuple, List
from . import Database


class Quotes(Database):
    __table_name: str = None

    def __init__(self):
        super().__init__()
        self.__table_name = "quotes"

    def create_table(self) -> None:
        query = f'''
            CREATE TABLE IF NOT EXISTS {self.__table_name} (
                id      SERIAL PRIMARY KEY,
                author    varchar(80) NOT NULL,
                quote  text
            )
        '''
        self.connect()

        self.cur.execute(query)
        self.commit()
        self.close()

    def insert_one(self, insert_values: Tuple) -> None:
        insert_script: str = f'INSERT INTO {self.__table_name}(author,quote) VALUES (%s,%s)'
        self.connect()
        self.cur.execute(insert_script, insert_values)
        self.commit()

    def find_all(self):
        query = f'SELECT * FROM {self.__table_name}'
        self.connect()
        self.cur.execute(query)
        return self.cur.fetchall()

    def count_all(self):
        query = f'SELECT COUNT(*) FROM {self.__table_name}'
        self.connect()
        self.cur.execute(query)
        return self.cur.fetchone()

    def find(self, quote_id: int) -> List:
        query = f'SELECT * FROM {self.__table_name} WHERE id = %s'
        self.connect()
        self.cur.execute(query, (quote_id,))
        return self.cur.fetchone()

    def drop_table(self):
        query = f'''
            DROP TABLE IF EXISTS {self.__table_name};
        '''
        self.connect()
        self.cur.execute(query)
        self.commit()
        self.close()
