import unittest
import data_io.file_storage as t


class TestFileStorage(unittest.TestCase):
    def setUp(self) -> None:
        f_s = t.FileStorage()

    def test_read_config_ok(self):
        f_s = t.FileStorage()
        self.assertEqual(f_s.read_config(['a'], './trash/'), [['a', '3']])

    def test_read_config_file_not_found(self):
        f_s = t.FileStorage()
        self.assertIsInstance(f_s.read_config([], '/qwe'), FileNotFoundError)

    def test_read_config_value_not_allowed(self):
        f_s = t.FileStorage()
        self.assertIsInstance(f_s.read_config([], '../'), ValueError)

    def test_read_config_send_ints(self):
        f_s = t.FileStorage(1)
        self.assertIsInstance(f_s.read_config(1, 1), FileNotFoundError)

    def test_read_config_send_none(self):
        f_s = t.FileStorage(None)
        self.assertIsInstance(f_s.read_config(None, None), FileNotFoundError)


unittest.TestCase()
