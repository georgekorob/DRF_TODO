import requests
from drftodo.settings import os

response = requests.post('http://127.0.0.1:8000/api-token-auth/',
                         data={'username': os.getenv('SUPER_USER_USERNAME'),
                               'password': os.getenv('SUPER_USER_PASSWORD')}
                         )

print(response.status_code)  # {'token': '2efa08beed5727856319740df3747df4e0a3655e'}
print(response.json())
