'''

__References__

Regular Expressions: Regexes in Python, Part 1 - https://realpython.com/regex-python/

regex has many functions available in the module "re" which are accessible
by using "import re" or more specifically "from re import module_name"

example function:
re.search(<regex>, <string>)

check out https://realpython.com/regex-python/ for good explanation of regex including metacharacters
'''

# from re import search
import re

# Scans a string for a regex match
# returns -  <re.Match object; span=(1, 4), match='767'>
username = 'm767doyle'
print(re.search('767', username))
find_username = re.search('767', username)
print(find_username)

# Regex metacharacters include ([]) e.g. ([0-9])
re.search('[0-9][0-9][0-9]', 'foo456bar')
find_digits = re.search('[0-9][0-9][0-9]', 'foo456bar')
print(re.search('[0-9][0-9][0-9]', 'foo456bar'))
print(find_digits)

# Regex metacharacters include '.' which acts as a wildcard
s = 'foo123bar'
re.search('1.3', s)
print(re.search('1.3', s))

greeting = "hello world"
print(re.search("[aeiou]", greeting))

print(re.search(r"x", "exit"))

print(re.search("[0-9]", "$100"))

print(re.search("[a-z]", "rhythm"))


