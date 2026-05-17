from sklearn.ensemble import RandomForestClassifier
class Model:
  def __init__(self):
    self.model = RandomForestClassifier()
  def train(self, X, y):
    self.model.fit(X, y)
  def predict(self, X):
    return self.model.predict(X)
python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
python
class Model:
  def __init__(self):
    # Load dataset
    self.data = pd.read_csv('data/dataset.csv')
    # Preprocess data (assuming last column is target variable)
    self.X = self.data.iloc[:, :-1]
    self.y = self.data.iloc[:, -1]

python
from sklearn.model_selection import train_test_split
class Model:
  # ...
  def __init__(self):
    # ...
    # Split data into training and testing sets
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
python
class Model:
  # ...
  def __init__(self):
    # ...
    # Define hyperparameters for tuning
    self.param_grid = {'n_estimators': [10, 50, 100, 200],
                       'max_depth': [None, 5, 10, 15]}
python
from sklearn.model_selection import GridSearchCV
class Model:
  # ...
  def __init__(self):
    # ...
    # Perform hyperparameter tuning using GridSearchCV
    self.grid_search = GridSearchCV(RandomForestClassifier(), self.param_grid, cv=5)
    self.grid_search.fit(self.X_train, self.y_train)
    # Get best estimator
    self.model = self.grid_search.best_estimator_
python
class Model:
  # ...
  def train(self, X_train, y_train):
    self.model.fit(X_train, y_train)
