from configs.config import Config
from data.utils import load_data
from models.model import Model
def main():
  """
  Main function.
  """
  # Load the configuration file
  config = Config('configs/config.json')
  
  # Load the dataset
  data = load_data('data/dataset.csv')
  
  # Initialize and train the model
  model = Model()
  model.train(data[:, :-1], data[:, -1])
if __name__ == '__main__':
  main()
