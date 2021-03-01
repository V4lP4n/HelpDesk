from data_io.file_storage import FileStorage
from data_io.logs import Logger
from data_io.db import DataBaseIO


class Kernel:
    def __init__(self, allowed_conf):
        # initializing config from ./config
        self.allowed_conf = allowed_conf
        self.files = FileStorage()
        self.config = {}
        try:
            for key, value in self.files.read_config(allowed_conf):
                self.config[key] = value
        except TypeError:
            raise self.files.read_config(allowed_conf)

        # initializing logger
        self.logger = Logger(self.config['logs_path'])
        self.logger.log('main successfully initiated', 'main', 'info')

        # initializing database
        self.db = DataBaseIO(self.config['db_type'], self.config['db_address'])
        if isinstance(self.db.connection, TypeError):
            self.logger.log(self.db.connection, 'main', 'error')
            raise self.db.connection

        self.db_conf = self.files.parse_json(self.config['db_conf'])

        self.db.db_prep(self.db_conf)



if __name__ == '__main__':

    allowed_conf = ['db_type',
                    'logs_path',
                    'db_address',
                    'db_conf']

    app = Kernel(allowed_conf)
