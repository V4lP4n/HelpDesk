from data_io.file_storage import FileStorage
from data_io.logs import Logger
from data_io.db import DataBaseIO


if __name__ == '__main__':
    # initializing config from ./config
    allowed_conf = ['db_type',
                    'logs_path',
                    'db_address']
    files = FileStorage()
    config = {}
    try:
        for key, value in files.read_config(allowed_conf):
            config[key] = value
    except TypeError:
        raise files.read_config(allowed_conf)

    # initializing logger
    logger = Logger(config['logs_path'])
    logger.log('main successfully initiated', 'main', 'info')

    # initializing database
    db = DataBaseIO(config['db_type'], config['db_address'])
    if isinstance(db.connection, TypeError):
        logger.log(db.connection, 'main', 'error')
        raise db.connection











