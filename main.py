from data_io.file_storage import FileStorage
from data_io.logs import Logger


if __name__ == '__main__':
    # initializing config from ./config
    allowed_conf = ['db_type', 'logs_path']
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







