'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

my_dict = {}
x = input('Please enter your feedback: ')
x = x.replace(" ", "")

for i in x:
    z = x.count(i)

    my_dict[i] = z
print(my_dict)

