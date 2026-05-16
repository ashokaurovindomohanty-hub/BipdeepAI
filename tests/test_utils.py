import unittest
from src.utils.api_utils import call_api
class TestUtils(unittest.TestCase):
  def test_call_api(self):
    response = call_api('https://example.com', 'api_key')
    self.assertIsNotNone(response)
