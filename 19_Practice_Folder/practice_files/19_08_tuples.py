
'''
__ References __


__ Glossary __

There are four collection data types in the Python programming language:
_ 'List' is a collection which is ordered and changeable. Allows duplicate members.
_ 'Tuple' is a collection which is ordered and unchangeable. Allows duplicate members.
_ 'Set' is a collection which is unordered and unindexed. No duplicate members.
_ 'Dictionary' is a collection which is unordered, changeable and indexed. No duplicate members

** Tuples are similar to lists, in that they can hold any other datatype,
  however, just like strings, they are immutable.
** Tuples are immutable, and usually, contain a heterogeneous sequence of elements
  - accessed via unpacking [...].
** Tuples are created by simply separating values by commas in an assignment,
   or by explicitly wrapping the values into brackets
** Lists are mutable, can hold any datatype and their elements are usually homogeneous
  - accessed by iterating over the list
  - created by enclosing values within square brackets
** Sets are an unordered collection with no duplicate elements
    - Basic uses include membership testing and eliminating duplicate entries.
    - Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
    - created by enclosing values within curly braces or by using the set()function
    - You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
     But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
      by using the in keyword.
    - Once a set is created, you cannot change its items, but you can add new items or remove items.

 mutable or immutable? how to access?
** Dictionaries are mutable or immutable? how to access?


** Creating a Tuple: t = 12345, 54321, 'hello!'
** Creating a List: bucket_list = ['climb Mt. Everest', 'eat fruits from a tree', 'raise a child']
*** Creating a Set:
*** Creating a Dictionary:

'''
# Tuples can be created either by simply separating values by
# commas in an assignment, or by explicitly wrapping the values into brackets


t = 12345, 54321, 'hello!'
print(t[0])

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u[1])



# Tuples are immutable i.e. you cannot add other items to them or remove items or change them
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v[1])

empty = ()
print(len(empty))
# 0
singleton = 'hello',  # <-- note trailing comma
print(len(singleton))
# 1
print(singleton)
# ('hello',)

# Updating Tuples

# Tuples are immutable which means you cannot update or
# change the values of tuple elements.
# Removing individual tuple elements is not possible.
# It is possible though to put together another tuple with the undesired elements discarded.
# In fact, tuples respond to all of the general sequence operations we used on strings in the prior chapter
#You are able to take portions of existing tuples to
# create new tuples as the following example demonstrates :

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = ('mars', 'venus','jupiter')
tup4 = ('mercury', 'earth', 'saturn')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup5 = tup1 + tup2;
print (tup5)
tup6 = tup4 + tup3
print(tup6)

# deleting an entire tuple
tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
del tup
print ("After deleting tup : ")
#print (tup)

weather = ('rain', 'clouds', 'sun', 'hail', 'wind')

print(weather[0:1])

'''
Built-in Tuple Functions
'''

print(len(tup4))

print(max(tup2))
print(min(tup2))


x = 1, 2
print((x))


