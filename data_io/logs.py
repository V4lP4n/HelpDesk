import logging
from data_io.file_storage import FileStorage


class Logger:
    def __init__(self, logs_path):
        self.logs_path = logs_path

    def log(self, message, source, log_type):
        try:
            # don't even try absolute paths
            if self.logs_path.startswith('/'):
                raise PermissionError

            # creating config and try to logging
            logging.basicConfig(filename=self.logs_path + source + '.log',
                                format='%(asctime)s %(message)s',
                                datefmt='%d/%m/%Y %I:%M:%S %p',
                                level=logging.DEBUG)
            if log_type == 'info':
                logging.info(message)
            elif log_type == 'error':
                logging.error(message)

            else:
                err = ValueError('wrong type of logs')
                raise err

        except PermissionError as err:
            return err
        except ValueError as err:
            return err
        except FileNotFoundError as err:
            return err


if __name__ == '__main__':
    ll = Logger('../storage/logs/')
    ll.log('its alive', '__file__', 'error')