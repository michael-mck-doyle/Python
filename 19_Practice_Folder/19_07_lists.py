

# creating a list
bucket_list = ['climb Mt. Everest', 'eat fruits from a tree', 'raise a child']
print(bucket_list[0])  # this is how we can access individual items in the list

# let's see how lists are *mutable* by changing the second item
bucket_list[1] += ' that I planted'
print(bucket_list[1])

print(bucket_list[2])

# ---- continuing the codeblock from above ---- #
# adding another item to the initial list above
bucket_list += ['live in Barcelona', 'work at Google']

print(bucket_list)
# notice that we are changing bucket_list *without re-assigning* the variable
# this is due to the fact that we are *mutating* the list in place
bucket_list.remove(bucket_list[-1])

print(bucket_list)

#Aliaising - Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:
a = [81, 82, 83]
b = a
print(a is b)

a = [81, 82, 83]
b = [81, 82, 83]

print(a == b)
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)