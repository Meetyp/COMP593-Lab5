import requests

def fetch_pokemon_info(name):
    pokemon_name=str(name).strip().lower()
    POKE_URL=f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    resp_msg=requests.get(POKE_URL)

    print(f"Getting information for {pokemon_name}...",end='')
    pokemon_dict = {}
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        pokemon_dict = body_dict
        return pokemon_dict

    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")
         
    pass
