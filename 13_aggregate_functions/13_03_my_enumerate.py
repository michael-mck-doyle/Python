'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index


More details on enumerate function:
https://docs.python.org/3.8/library/functions.html#enumerate

Using enumerate function is equivalent to writing:
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

'''


def my_enumerate(x, start = 1):
    n = start
    for i in x:     # where x is the sequence, list..
        yield n, i
        n += 1


names = ["John", "Grace", "Zac", "Chrissy", "Reynaldo", "Gemima"]
enum = my_enumerate(names, start=1)

for i in enum:
    print(i)



my_list = ["apple", "banana", "orange"]
new_list = []
obj1 = enumerate(my_list)
print(obj1)

for i in (obj1):
    new_list.append(i)
print(new_list)



