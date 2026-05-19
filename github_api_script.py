import requests
import os
api_key = os.environ['GITHUB_API_KEY']
url = "https://api.github.com/user/repos"
headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get(url, headers=headers)
print(response.json())