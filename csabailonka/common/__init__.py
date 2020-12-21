from csabailonka.common import config

VERSION = '0.0.1'

def apply_defaults():
    config.for_logging()
    config.for_properties()