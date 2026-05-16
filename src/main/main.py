from configs.config import Config
from data.utils import load_data
from models.model import Model
def main():
  config = Config('configs/config.json')
  data = load_data('data/dataset.csv')
  model = Model()
  model.train(data[:, :-1], data[:, -1])
if __name__ == '__main__':
  main()
