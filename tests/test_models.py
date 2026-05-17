python
import unittest
from models.model import Model
class TestModel(unittest.TestCase):
  def setUp(self):
    self.model = Model()
  def test_init(self):
    self.assertIsNotNone(self.model.data)
    self.assertIsNotNone(self.model.X)
    self.assertIsNotNone(self.model.y)
  def test_train(self):
    self.model.train(self.model.X, self.model.y)
    self.assertIsNotNone(self.model.model)
