import sqlite3


class DataBaseIO:
    def __init__(self, db_type, db_address):
        self.db_type = db_type
        self.db_address = db_address
        self.connection = ''

        if self.db_type == 'SQLite':
            connection = self._connect_sqlite()
        else:
            connection = TypeError('Not supported database type')

        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_handler(self, data, table):
        if self.db_type == 'SQLite':
            self._get_sqlite(data, table)

    def db_prep(self, conf):
        print(conf)
        for table in conf['tables']:
            fields = ''

            for key, value in conf['tables'][table].items():
                fields += key + ' ' + value + ','

            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} ({fields[:-1]})')

    def _get_sqlite(self, data, table):
        pass

    def _connect_sqlite(self):
        try:
            db = sqlite3.connect(self.db_address)

        except sqlite3.OperationalError as err:
            return err

        return db

