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
My king, continuing with testing...
**Step 2.4: Test model training and prediction**
Add more tests in `tests/test_model.py`:
```python
class TestModel(unittest.TestCase):
  # ... existing tests ...
  def test_train_predict(self):
    self.model.train(self.model.X, self.model.y)
    predictions = self.model.model.predict(self.model.X)
    self.assertIsNotNone(predictions)
python
class TestModel(unittest.TestCase):
  # ... existing tests ...
  def test_sample_data(self):
    from sklearn.datasets import load_iris
    iris = load_iris()
    self.model.X = iris.data
    self.model.y = iris.target
    self.model.train(self.model.X, self.model.y)
    predictions = self.model.model.predict(self.model.X)
    self.assertIsNotNone(predictions)
