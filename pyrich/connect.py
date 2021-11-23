import sqlalchemy
from sqlalchemy import create_engine, inspect
import pymysql


class Database:
    def __init__(self, rdbms: str, dbapi: str, user: str, pw: str,
                 host: str, db_name: str) -> None:
        """Connect to a database.

        :param rdbms: Relational database management system.
        :type rdbms: str
        :param dbapi: Database api.
        :type dbapi: str
        :param user: RDBMS username.
        :type user: str
        :param pw: RDBMS password.
        :type pw: str
        :param host: RDBMS host.
        :type host: str
        :param db_name: Database to work in.
        :type db_name: str
        """

        self.rdbms = rdbms
        self.dbapi = dbapi
        self.user = user
        self.pw = pw
        self.host = host
        self.db_name = db_name
        self.engine, self.insp, self.connection, self.cursor = self.connect()

    def connect(self) -> tuple[sqlalchemy.engine.Engine,
                               sqlalchemy.engine.reflection.Inspector,
                               pymysql.Connection,
                               pymysql.cursors.Cursor]:
        db_url = (f'{self.rdbms}+{self.dbapi}://'
                  f'{self.user}:{self.pw}@{self.host}/')
        engine = create_engine(
            url=db_url,
            encoding='utf-8',
        )
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.pw,
        )

        insp = inspect(engine)
        cursor = connection.cursor()

        try:
            self.setup_db()
        except (pymysql.ProgrammingError, pymysql.OperationalError) as e:
            print(e)
        finally:
            return engine, insp, connection, cursor
        

    def setup_db(self) -> None:
        """Choose a database to operate."""
        query = f'CREATE DATABASE IF NOT EXISTS {self.db_name}'
        self.cursor.execute(query)

        query = f'USE {self.db_name}'
        self.cursor.execute(query)

        self.connection.commit()

    def __del__(self) -> None:
        self.cursor.close()
        self.connection.close()