import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6bd346914a4f217970f01112b7b96679'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 5134
def test_status_code():
    response = requests.get (url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response_trainer_id():
    response_get = requests.get (url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"] [0] ["trainer_id"] == str(TRAINER_ID)