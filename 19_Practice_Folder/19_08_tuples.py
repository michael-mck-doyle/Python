
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


