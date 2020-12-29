import unittest

class TestConfig(unittest.TestCase):
    def test_for_logging(self):
        from csabailonka.common import config as default_config
        default_config.for_logging()
        self.assertTrue(True)

    def test_for_properties(self):
        from pathlib import Path
        from csabailonka.common import config as default_config
        with self.assertRaises(ValueError):
            default_config.for_properties(Path('does_not_exist.json'))