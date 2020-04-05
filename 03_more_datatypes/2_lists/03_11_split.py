'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

from itertools import count

from collections import Counter

txt = input("write a sentence containing repeating words: ")

b = txt.split(" ")

b = Counter(b)

for w in b:
    c = b.count(w)
    print(w, c)
    x = w
    y = c
str_dict = []
str_dict.update({x:y})

print(str_dict)

print("The word with the most occurrences is: ", max(b))


'''
for w in b:
    print ('%s : %d' % (w, b[w]))
print()

'''




