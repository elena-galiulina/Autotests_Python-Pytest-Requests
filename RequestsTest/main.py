import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6bd346914a4f217970f01112b7b96679'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_response_new_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 1
}

response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_response_new_name)
print(response_new_name.text)

body_response_in_pokeball = {
    "pokemon_id": pokemon_id
}
response_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_response_in_pokeball)
print(response_in_pokeball.text)