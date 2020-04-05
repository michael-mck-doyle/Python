'''
Write a script that takes a list and turns it into a tuple.

'''


txt = input("write a sentence containing repeating words: ")

b = txt.split(" ")

print("list: ", b)
print()
b = tuple(b)

print("tuple: ", b)
print()

b = list(b)
print("list: ", b)

