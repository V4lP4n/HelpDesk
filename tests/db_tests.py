import unittest
import data_io.db as db
import sqlite3


class TestDB(unittest.TestCase):

    def test_db_ok_sqlite(self):
        b = db.DataBaseIO('SQLite', './trash/test.db')
        self.assertIsInstance(b, db.DataBaseIO)

    def test_db_file_not_found(self):
        b = db.DataBaseIO('SQLite', './non_existing_folder/test.db')
        self.assertIsInstance(b.connection, sqlite3.OperationalError)

    def test_db_file_non_existing_db_type(self):
        b = db.DataBaseIO('Non_existing Type', './non_existing_folder/test.db')
        self.assertIsInstance(b.connection, TypeError)

    def test_db_send_ints(self):
        b = db.DataBaseIO(1, 1)
        self.assertIsInstance(b.connection, TypeError)

    def test_db_send_nones(self):
        b = db.DataBaseIO(None, None)
        self.assertIsInstance(b.connection, TypeError)


