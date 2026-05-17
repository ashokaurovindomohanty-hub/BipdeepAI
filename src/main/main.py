from configs.config import Config
from data.utils import load_data
from models.model import Model
def main():
  model = Model()
  # Load the configuration file
  config = Config('configs/config.json')
  # Initialize and train the model
  model.train(model.X, model.y)
