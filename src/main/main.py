from configs.config import Config
from data.utils import load_data
from models.model import Model
def main():
  model = Model()
  # Load the dataset
  data = load_data('data/dataset.csv')
  model.X = data.iloc[:, :-1]
  model.y = data.iloc[:, -1]
  # Load the configuration file
  config = Config('configs/config.json')
  # Initialize and train the model
  model.train(model.X, model.y)
if __name__ == '__main__':
  main()
