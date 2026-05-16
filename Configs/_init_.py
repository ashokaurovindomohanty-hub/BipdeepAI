import json
class Config:
  def __init__(self, file_path):
    self.file_path = file_path
    self.config = json.load(open(file_path))
  def get_api_key(self):
    return self.config['api_key']
  def get_database_url(self):
    return self.config['database_url']
