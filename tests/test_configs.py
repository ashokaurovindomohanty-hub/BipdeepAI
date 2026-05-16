import unittest
from configs.config import Config
class TestConfigs(unittest.TestCase):
  def test_config(self):
    config = Config('configs/config.json')
    self.assertIsNotNone(config.get_api_key())
