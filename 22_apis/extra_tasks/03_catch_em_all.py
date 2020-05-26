'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''

import requests
from pprint import pprint
import json
'''
response = requests.get("https://pokeapi.co/docs/v2.html#pokemon")
#print(response.status_code)
#pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")
data = response.json()
print(data)

print()

'''
params = {
    "color": "#f5871f", #returns user based on email address

}

response = requests.get("https://pokeapi.co/docs/v2.html#pokemon", params=params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")