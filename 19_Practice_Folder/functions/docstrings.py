'''
You should always aim to write docstrings for the code you produce.

Docstrings describe:
    - what the function is about
    - what are the arguments it takes
    - what output it produces
'''

mock_input = "hello hello my name's dibo"


def titlecase(text):
    """
    titlecase capitalises the first letter in every word in a sentence
    """
    titlecase = []
    for word in mock_input.split():
        word = word.capitalize()
        titlecase.append(word)

    print(titlecase)
    return " ".join(titlecase)


print(titlecase(mock_input))

# calling docstrings for a function using ".__doc__" format - 1
print(titlecase.__doc__)

# calling docstrings for a function using "help(function_name)" - 2
print(help(titlecase))

'''
def km_to_miles(km):
    """Converts kilometers to miles.

    Args:
    km (float): An amount of kilometers, can also be int

    Returns:
    float: The converted amount in miles
    """
    miles = km * 0.6
    return miles


print(km_to_miles.__doc__)

# also attempt to run the help() function
# help(km_to_miles)

'''





