import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5f10b5b0f4fad7776f94c849955de66c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 4537

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_get_trainers_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert 'Райден' in response.text