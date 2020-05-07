'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''

x = [1, 2, 3]
y = ["a", "b", "c"]

try:
    while x < y:
        print(y)
except TypeError as e:
    print("'<' not supported between instances of 'int' and 'str'", e)
