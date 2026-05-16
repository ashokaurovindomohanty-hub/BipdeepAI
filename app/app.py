from flask import Flask, jsonify
from src.main import main
app = Flask(__name__)
@app.route('/api/predict', methods=['POST'])
def predict():
  output = main()
  return jsonify({'output': output})
if __name__ == '__main__':
  app.run()
