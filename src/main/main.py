from configs.config import Config
from data.utils import load_data
from models.model import Model
def main():
  model = Model()
  # Load the configuration file
  config = Config('configs/config.json')
  # Initialize and train the model
  model.train(model.X, model.y)
if __name__ == '__main__':
  main()
```
**models/model.py**
```python
from data.utils import load_data
from sklearn.ensemble import RandomForestClassifier
class Model:
  def __init__(self, file_path='data/dataset.csv'):
    # Load dataset
    self.data = load_data(file_path)
    # Split data into features (X) and target variable (y)
    self.X = self.data.iloc[:, :-1]
    self.y = self.data.iloc[:, -1]
    self.model = RandomForestClassifier()
  def train(self, X, y):
    self.model.fit(X, y)
