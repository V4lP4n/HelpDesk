from pathlib import Path


class FileStorage:

    def __init__(self, workdir=Path.cwd()):
        self.workdir = str(workdir)

    def read_config(self, allowed_conf, conf_path=''):
        """Try to read config file and return values or error"""
        allowed_conf, conf_path = str(allowed_conf), str(conf_path)
        try:
            with open(conf_path + 'config') as conf:
                keys = []
                line_number = 1
                for line in conf.readlines():
                    line = line.replace(' ', '')
                    line = line.replace('\n', '')
                    key, value = line.split('=')
                    if key in allowed_conf:
                        keys.append([key, value])
                    else:
                        err = ValueError(f'Config param {key}, not in allowed conf, '
                                         f'please check your config file at line {line_number}.')
                        return err
                    line_number += 1

            return keys
        except FileNotFoundError as err:
            return err


