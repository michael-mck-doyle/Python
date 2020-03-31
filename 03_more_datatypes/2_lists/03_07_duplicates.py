'''

Write a script that removes all duplicates from a list.

'''

my_list = [1, 2, 3, 4, 3, 4, 5]

my_list = list(dict.fromkeys(my_list))
print(my_list)

