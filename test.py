# Information from PokéAPI obtained through PokeBase
# PokeAPI: https://pokeapi.co/
# PokeBase: https://github.com/PokeAPI/pokebase
import pokebase as pb
import json
import pprint
from urllib.request import Request, urlopen

# Output generation for a Pokémon species(name or id) or berry (name or id)
def getWebpage(loader):
    url = loader.url
    # All info of a loader is stored in url.
    req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    # Decoding is done to convert bytes into a dictionary
    webpage.decode('utf-8')
    return webpage

# Main asks user for input then calls getWebpage, or prints out a list of all Pokémon. 
# User is only asked for these three options to keep the test simple.
def main():
    # pprint used to help format output neatly.
    pp = pprint.PrettyPrinter(indent = 2)
    while(True):
        print('Welcome!')
        print('1. Get data for a specific berry.')
        print('2. Get data for a specific Pokemon species.')
        print('3. Get a list of Pokemon or berries.')
        print('4. Exit program.')
        print('Enter a number corresponding to the options listed above...')
        x = (int) (input())
        if(x == 1): # Berry data
            # Input can either be a specified berry name or id number (1-64).
            # Input will assume you are entering the correct information.
            # Note: As of now data for roseli berry, kee berry, and maranga berry cannot be accessed.
            berry = input('Enter a berry name (ex. oran) or id number (1-64): ')
            loader = pb.berry(berry)
            berry_data = json.loads(getWebpage(loader))

            pp.pprint(berry_data)
        
        elif(x == 2): # Pokémon species data. Note: Long output.
            # Input assumes you are entering the correct information.
            # As of now, according to the national pokedex, there are 893 Pokémon but that is subject to change.
            # Warning: long output.
            pokemon_species = input('Enter a pokemon species (ex. wormadam) name or id number (1-893): ')
            loader = pb.pokemon_species(pokemon_species)
            pokemon_species_data = json.loads(getWebpage(loader))

            pp.pprint(pokemon_species_data)

        elif(x == 3): # Pokémon or berry list
            # Input assumes you are entering the correct information.
            # Note: pokemon and berry are not the only groups that can be called and outputted asked for simplicity
            # Check documentation and for more information on what can be entered.
            # Warning: long output.
            # Not formatted neatly
            group_list = input('Enter "pokemon" or "berry": ')
            
            print(pb.APIResourceList(group_list))
        
        elif(x == 4):
            print('Have a nice day!')
            break
        
        else:
            print('Input invalid. Please try again.')



if(__name__ == '__main__'):
    main()