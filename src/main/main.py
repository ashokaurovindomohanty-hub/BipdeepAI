from utils.api_utils import call_api
from utils.data import load_data
from models.model import Model
def main():
  model = Model()
  # Load the configuration file
  config = Config('configs/config.json')
  # Initialize and train the model
  model.train(model.X, model.y)
if __name__ == '__main__':
  main()
