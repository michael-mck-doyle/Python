'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''


r = (input("Please enter a string of words: "))
s = (input("Please enter a letter: "))
r = r.lower()
f = r.find(s)

print(f)
print(r)


