'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

from random import randrange
x = 0
my_num_list = []
next_num_list = []

while x < 20:
    y = (randrange(1, 100))
    print(y)
    my_num_list.append(y)
    x += 1
print(my_num_list)

# create individual tuples by slicing the list

while x <= len(my_num_list):
    z = my_num_list[0:20:10]
    t = next_num_list.append(z)

    print(my_tuple)

    x += 1



# add the individual tuples back to new list
'''
print(my_num_list)

my_tuple = tuple(my_num_list)
print(my_tuple)

for i in my_num_list:
    while x <= len(my_num_list):
        y = my_num_list.split(' , ')
        print(y)
'''
