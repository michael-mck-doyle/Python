'''
use the 'import' keyword to enable access to certain functions within libraries

use the dir() function to list all of the modules/functions within a library e.g. print(dir(math))
'''

import urllib
print('urllib Functions/Modules')
u = dir(urllib)
for i in u:
    print(i)

print()
import requests
print('requests - The requests library is the de facto standard for making HTTP requests in Python - https://realpython.com/python-requests/')
r = dir(requests)
for i in r:
    print(i)


print()
print('Keywords Functions/Modules')
import keyword

k = dir(keyword)
for i in k:
    print(i)


#print(keyword.iskeyword)
#print(keyword.kwlist)

import math

print()
print('Maths Functions/Modules')
m = dir(math)
for i in m:
    print(i)


print()
print('Statistics Functions/Modules')
import statistics

s = dir(statistics)
for i in s:
    print(i)







