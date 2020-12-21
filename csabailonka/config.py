import json
import logging
import os
from pathlib import Path
from types import SimpleNamespace


def for_logging(filename='logs/app.log',
                filemode='w+',
                level=logging.DEBUG,
                logFormat='%(asctime)s :: %(levelname)-5s :: %(threadName)-24s :: %(name)-24s - %(message)s'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    logging.basicConfig(filename=filename, filemode=filemode, level=level, format=logFormat)

def for_properties(path=Path('config.json')):
    """
    Simple externalized configuration loader. Properties are loaded from a file containing a JSON object.
    :param path: Path to the file.
    :return: Simple namespace with the key/value pairs matching the loaded json object.
    """
    if not path or not path.exists():
        raise ValueError(f"Configuration file [{path}] doesn't exist")
    return json.loads(path.read_text(), object_hook=lambda d: SimpleNamespace(**d))