'''
use the 'import' keyword to enable access to certain functions within libraries

use the dir() function to list all of the modules/functions within a library e.g. print(dir(math))


There are a lot of built-in modules in Python. Some of the important ones are – collections, datetime,
 logging, math, numpy, os, pip, sys, and time. You can execute help('modules') command in Python shell
  to get the list of available modules. - from https://www.journaldev.com/14329/python-modules

'''
# Global variables
print("Global variables")
e = dir(globals())
f = ()
for i in e:
    print(i)


print()
print()

# Local variables
print("Local variables")
e = dir(globals())
f = ()
for i in e:
    print(i)

print()
print()

#unittest
import unittest
print('unittest Functions/Modules')
e = dir(unittest)
f = ()
for i in e:
    print(i)

print()
print()

# enumerate
print('enumerate Functions/Modules')
e = dir(enumerate)
f = ()
for i in e:
    print(i)

print()
print()

import logging
print('collections Functions/Modules')
l = dir(logging)
for i in l:
    print(i)

print()
print()


import collections
print('collections Functions/Modules')
c = dir(collections)
for i in c:
    print(i)

print()
print()

import time
print('time Functions/Modules')
t = dir(time)
for i in t:
    print(i)

print()
print()

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
print()

import string
print('String Functions/Modules')
s = dir(str)
for i in s:
    print(i)

print()
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







