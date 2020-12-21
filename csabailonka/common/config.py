import json
import logging
import os
from pathlib import Path
from types import SimpleNamespace


def for_logging(filename: str = 'logs/app.log',
                filemode: str = 'w+',
                level: int = logging.DEBUG,
                logFormat: str = '%(asctime)s :: %(levelname)-5s :: %(threadName)-24s :: %(name)-24s - %(message)s',
                loggers=None):
    """
    Preconfigures the default python logger with the provided parameters.
    :param filename: Log file name. Can include directory structure.
    :param filemode: File opening mode for the logfile.
    :param level: Default log level.
    :param logFormat: Log string format.
    :param loggers: List of logger name & log level tuples, used to preconfigure certain loggers.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    logging.basicConfig(filename=filename, filemode=filemode, level=level, format=logFormat)
    if loggers:
        for logger, level in loggers:
            logging.getLogger(logger).setLevel(level)

def for_properties(path: Path = Path('config.json')):
    """
    Simple externalized configuration loader. Properties are loaded from a file containing a JSON object.
    :param path: Path to the file.
    :return: Simple namespace with the key/value pairs matching the loaded json object.
    """
    if not path or not path.exists():
        raise ValueError(f"Configuration file [{path}] doesn't exist")
    return json.loads(path.read_text(), object_hook=lambda d: SimpleNamespace(**d))