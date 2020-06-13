'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the area of the two countries differ?
* Print the native name of both countries, as well as their capitals
https://restcountries.eu/rest/v2/{service}?fields={field};{field};{field}
https://restcountries.eu/rest/v2/all?fields=name;capital;currencies

'''

import requests
from pprint import pprint

print()
print("Action Menu:")

country = input("Please enter the name of a country: ")
param_1 = input("PLease enter a filter: ")

#params = {
 #   "field1": param_1
#}

base = "https://restcountries.eu/rest/v2/name/"
#params

response = requests.get(base+country, params=param_1)

pprint(response.status_code)
pprint(response.encoding)
pprint(response.content)
pprint(response.headers)

# population
# size (area)
# native name
# capital
# 1. ask user to input the name of two countries they would like to do a comparison of
# 2. the countries will be parameters in the method get requests
# 3. GET individual information for a country or request all of the data and then parse it
# 4. extract the information from the two countries and print to screen
# 5. do a comparison of the aforementioned data features and print the results
