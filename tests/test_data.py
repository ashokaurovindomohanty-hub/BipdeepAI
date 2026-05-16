import unittest
from data.utils import load_data
class TestDatas(unittest.TestCase):
  def test_load_data(self):
    data = load_data('data/dataset.csv')
    self.assertIsNotNone(data)
