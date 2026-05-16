import unittest
from models.model import Model
class TestModels(unittest.TestCase):
  def test_model(self):
    model = Model()
    self.assertIsNotNone(model)
