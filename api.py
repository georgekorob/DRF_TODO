import requests
import time
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

DOMAIN = 'http://127.0.0.1:8000'


def timeout():
    time.sleep(2)


def get_url(url):
    return f'{DOMAIN}{url}'


timeout()

# не авторизован
response = requests.get(get_url('/api/projects/'))
assert response.status_code == 401

timeout()
# response = requests.post(get_url('/api-token-auth/'), data={'username': os.getenv('SUPER_USER_USERNAME'),
#                                                             'password': os.getenv('SUPER_USER_PASSWORD')})
# базовая авторизация
response = requests.get(get_url('/api/projects/'), auth=(os.getenv('SUPER_USER_USERNAME'),
                                                         os.getenv('SUPER_USER_PASSWORD')))
assert response.status_code == 200

timeout()
# авторизация по токену
TOKEN = 'e8da340a90986eb33d5bea49d4e1ac8568f2a5e9'
# response = requests.get(get_url('/api/projects/'), headers={'Authorization': f'Token {TOKEN}'})
headers = {'Authorization': f'Token {TOKEN}'}
response = requests.get(get_url('/api/projects/'), headers=headers)
assert response.status_code == 200

timeout()

# авторизация по jwt
# Получаем токен
response = requests.post(get_url('/api/token/'), data={'username': os.getenv('SUPER_USER_USERNAME'),
                                                       'password': os.getenv('SUPER_USER_PASSWORD')})
result = response.json()
# это наш токен
access = result['access']
print('Первый токен', access, end=f'\n{150 * "*"}\n')
# это для рефреша
refresh = result['refresh']
print('refresh', refresh, end=f'\n{150 * "*"}\n')
timeout()
# Авторизуемся с ним
headers = {'Authorization': f'Bearer {access}'}
response = requests.get(get_url('/api/projects/'), headers=headers)
assert response.status_code == 200

timeout()
# Рефрешим токен ( ДЛЯ ОБНОВЛЕНИЯ)
response = requests.post(get_url('/api/token/refresh/'), data={'refresh': refresh})
# print(response.status_code)
# print(response.text)
result = response.json()
# это наш токен
access = result['access']
print('Обновленный токен', access, end=f'\n{150 * "*"}\n')
print('refresh', refresh, end=f'\n{150 * "*"}\n')
timeout()
# Авторизуемся с ним
headers = {'Authorization': f'Bearer {access}'}
response = requests.get(get_url('/api/projects/'), headers=headers)
assert response.status_code == 200
