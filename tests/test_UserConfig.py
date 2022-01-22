from unittest import TestCase

from UserConfig import Config


class TestConfig(TestCase):
    def test_config_from_file(self):
        config = Config.configFromFile()
        self.assertIsNotNone(config)
