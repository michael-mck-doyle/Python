'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
from itertools import count

a = input("write a sentence containing repeating words: ")


b = a.split(" ")

print(b)


for w in b:
    c = b.count(w)
    print(w, c)
    x = w
    y = c
str_dict = {}
str_dict.update({x:y})

print(str_dict)







