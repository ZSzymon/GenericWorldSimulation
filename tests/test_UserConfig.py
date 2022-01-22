from unittest import TestCase

from userConfig import Config


class TestConfig(TestCase):
    def test_config_from_file(self):
        config = Config.configFromFile()
        self.assertIsNotNone(config)
