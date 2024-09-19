import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5f10b5b0f4fad7776f94c849955de66c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_born_pokemons = {
    "name": "Балли9",
    "photo_id": 9
}

body_rename_pokemon = {
    "pokemon_id": "72709",
    "name": "Балли Нью9",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "72709"
}
'''response_born_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_born_pokemons)
message = response_born_pokemon.json()['message']
print(message)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename_pokemon)
message = response_rename.json()['message']
print(message)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)

