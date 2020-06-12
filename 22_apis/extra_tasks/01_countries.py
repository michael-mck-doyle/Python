'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the area of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
import requests
from pprint import pprint

base = "https://restcountries.eu/rest/v2/name/philippines"


response = requests.get(base)

pprint(response.status_code)
pprint(response.encoding)
pprint(response.content)
pprint(response.headers)

# population
# size (area)
# native name
# capital
# 1. extract the information from the two countries and print to screen
# 2. do a comparison of the aforementioned data features and print the results
