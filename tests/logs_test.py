import unittest
import data_io.logs as lo


class TestLogger(unittest.TestCase):

    def test_logs_ok(self):
        log = lo.Logger('./ok')
        self.assertEqual(log.log('ok', 'tests', 'error'), None)

    def test_logs_file_not_found(self):
        log = lo.Logger('./notok/err')
        self.assertIsInstance(log.log('err', 'tests', 'error'), FileNotFoundError)

    def test_logs_permission_err(self):
        log = lo.Logger('/')
        self.assertIsInstance(log.log('sad', 'tests', 'error'), PermissionError)

    def test_logs_wrong_type(self):
        log = lo.Logger('./etc:)')
        self.assertIsInstance(log.log('err', 'tests', 'err'), ValueError)


unittest.TestCase()
