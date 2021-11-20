from typing import Dict
from domain.interfaces import DatabaseConnectionInterface
from sqlite3 import connect, Error, Row
from sqlite3.dbapi2 import Connection, Cursor

class DatabaseConnection(DatabaseConnectionInterface):

    _connection: Connection = None
    _cursor: Cursor = None

    def connect(self):
        try:
            self._connection = connect(self.database)
            self._connection.row_factory = Row
        except Error as error:
            print("Ошибка при подключении к sqlite", error)

    def close(self):
        if (self._connection):
            self._connection.close()
            self._connection = None
            self._cursor = None
        print("Соединение с SQLite закрыто")

    def commit(self):
        self.connection.commit()

    def get(self) -> Dict[str, any]:
        return self.cursor.fetchall()

    def execute(self, query: str):
        self.cursor.execute(query)

    @property
    def cursor(self) -> Cursor:
        if not self._cursor:
            self._cursor = self.connection.cursor()
        return self._cursor

    @property
    def connection(self) -> Connection:
        if not self._connection:
            self._cursor = self.connect()
        return self._connection
