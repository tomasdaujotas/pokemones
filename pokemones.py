import requests
import random
import pandas as pd

idPokemonAleat = []

for i in range(10):
    aleat = random.randint(1, 890)
    idPokemonAleat.append(aleat)

pokemonList = []

for id in idPokemonAleat:
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'

    r = requests.get(url)
    rJson = r.json()

    pokemonData = {}

    #nombres
    pokemonData['name'] = rJson['name']

    #tipos
    pokemonTypes = []

    for t in rJson['types']:
        pokemonType = t['type']['name']
        pokemonTypes.append(pokemonType)

    pokemonData['types'] = pokemonTypes

    #habilidades
    pokemonAbilities = []

    for a in rJson['abilities']:
        pokemonAbility = a['ability']['name']
        pokemonAbilities.append(pokemonAbility)
    
    pokemonData['abilities'] = pokemonAbilities

    #estadisticas
    pokemonData['Hp'] = rJson['stats'][0]['base_stat']
    pokemonData['Attack'] = rJson['stats'][1]['base_stat']
    pokemonData['Defense'] = rJson['stats'][2]['base_stat']
    pokemonData['SpecialAttack'] = rJson['stats'][3]['base_stat']
    pokemonData['SpecialDefense'] = rJson['stats'][4]['base_stat']
    pokemonData['SpecialSpeed'] = rJson['stats'][5]['base_stat']

    pokemonList.append(pokemonData)

dfPokemon = pd.DataFrame(pokemonList)
dfPokemon.to_excel('pokemones.xlsx')