from unittest import TestCase

from settings import Settings

class TestConfig(TestCase):
    def test_config_from_file(self):
        config = Settings.config

        self.assertIsNotNone(config)
