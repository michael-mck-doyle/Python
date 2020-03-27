
'''
__ References __
Nested Lists - https://www.learnbyexample.org/python-nested-list/


__ Glossary __

** Nested List = A list can contain any sort object, even another list (sublist),
which in turn can contain sub-lists themselves, and so on. This is known as nested list.
You can use them to arrange data into hierarchical structures.  A nested list is created
by placing a comma-separated sequence of sublists.




'''


# creating a list
bucket_list = ['climb Mt. Everest', 'eat fruits from a tree', 'raise a child']
print(bucket_list[0])  # this is how we can access individual items in the list

# let's see how lists are *mutable* by changing the second item
bucket_list[1] += ' that I planted'
print(bucket_list[1])

bucket_list[0] += " with friends"
print(bucket_list)

print(bucket_list[2])

# ---- continuing the codeblock from above ---- #
# adding another item to the initial list above
bucket_list += ['live in Barcelona', 'work at Google']

print(bucket_list)
# notice that we are changing bucket_list *without re-assigning* the variable
# this is due to the fact that we are *mutating* the list in place
bucket_list.remove(bucket_list[-1])

print(bucket_list)

print("--------------------")
print("Aliaising")
print("_________")
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

print("------------------")
print("Accessing Values in Lists")
print("__________________")

ist1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


print("------------------")
print("Updating Lists")
print("__________________")
list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

print("------------------")
print("Deleting List Elements")
print("__________________")
# use the 'del' command and the index value to delete an element from a list

list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ")
print (list1)

print("------------------")
print("Methods for Lists")
print("__________________")

# - Appends object obj to list
list_fish = ['cod', 'halibut', 'haddock']
list_fish.append('mackeral')
print(list_fish)

# - Reverses objects of list in place
list_fish.reverse()
print(list_fish)

for task in list_fish:
    print(task)

#list.remove(item)
#list.sort()
#del(list[index])

numbers = [1, 2, 3]
#numbers.insert(1, 1)
#numbers.extend([4, 5])
#numbers += [4, 5]
# numbers.append(4)
print(numbers)

numbers = [42, 1, 10]
print(numbers)
numbers.extend([5])
print(numbers)
numbers.remove(1)
print(numbers)

aList = ['xyz', 'zara', 'abc', 'xyz']
aList.sort()
print(aList)

# Nested Lists
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[2])        # ['cc', 'dd', ['eee', 'fff']]
print(L[2][2])     # ['eee', 'fff']
print(L[2][2][0])  # eee

