from pastebin_api import post_new_paste
from poke_api import fetch_pokemon_info
import sys

def main():
    name = get_pokemon_name()
    pokemon_information = fetch_pokemon_info(name)

    if pokemon_information:
        title, body = create_info_for_paste(pokemon_information)
        post_url = post_new_paste(title,body,'1M')
        print(post_url)

def get_pokemon_name():
    params_length = len(sys.argv)-1
    if params_length > 0:
        return sys.argv[1]
    else:
        print(f"Error: Missing parameters.")
        sys.exit(1)

def create_info_for_paste(data):
    name_of_pokemon = data['name'].capitalize()
    abilities_of_pokemon = [j['ability']['name'] for j in data['abilities']]
    # print(abilities_of_pokemon)
    abilities_list_of_pokemon= '- ' + '\n- '.join(abilities_of_pokemon)
    title = f"{name_of_pokemon}'s Abilities"
    body = abilities_list_of_pokemon

    return (title, body)


if __name__ == '__main__':
    main()
