'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

my_list = [1, 2, 3, 4, 3, 4, 5]

unique_list = list(dict.fromkeys(my_list))
print(unique_list)


