'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)


See: itertools — Functions creating iterators for efficient looping
https://docs.python.org/3/library/itertools.html#itertools.product
itertools.product(*iterables, repeat=1)¶
Cartesian product of input iterables.

Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B)

'''

import itertools

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

try:

    cartesian_products = [(x, y) for x in colors for y in sizes]

    print("Using list comprehension: ", cartesian_products)
    print()
    # using itertools.product
    cartesian_products = [x for x in itertools.product(colors, sizes)]
    print("Using itertools.product in list comprehension: ", cartesian_products)

except TypeError as e:
    print(e)



