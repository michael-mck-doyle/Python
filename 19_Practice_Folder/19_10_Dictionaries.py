

'''
References - Dictionaries
5.5. Dictionaries - https://docs.python.org/3/tutorial/datastructures.html#dictionaries
Dictionary Methods - https://www.programiz.com/python-programming/methods/dictionary/copy
Python Dictionaries - https://www.w3schools.com/python/python_dictionaries.asp
'''


users = {'mary': 22, 'caroline': 26, 'harry': 22}

print(users['harry'])
# 22

# the lookup can also be used to update a value in a dict
users['harry'] = 20
print(users['harry'])
# 20

users['mary'] = 27
print(users['mary'])


users = {'mary': 22, 'caroline': 26, 'harry': 20}

# the dict.items() method yields a list of tuple objects
# that we can subsequently iterate over
for user, age in users.items():
    print(user, age)

'''
Dictonary Methods

examples of methods that can be used on Dictionaries can be found at:
https://www.programiz.com/python-programming/methods/dictionary/copy

'''
# clear method

d = {1: "one", 2: "two"}

d.clear()
print('d =', d)

# copy method

original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)

new_dict = {}
new_dict ["planet"] = "mars"
print(new_dict['planet'])
