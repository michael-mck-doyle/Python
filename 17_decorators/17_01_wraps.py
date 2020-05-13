'''
Write a decorator function that wraps text passed to it in a html <p> tag.
'''


# 1 - adding html tags - decorator practice
def wrap_up(initial_func):
    def wrapper_func():
        print(f"<p>{initial_func()}<p> ...wrapped")
    return wrapper_func()


@wrap_up
def publish():
    return "Headline news!"


# 2 - more decorator practice
def name_it(initial_func):
    def wrapper_func():
        print(f"{initial_func()}...is the perfect name!")
    return wrapper_func()


@name_it
def baby_name(name=input("Enter a baby name: ")):
    return name


@name_it
def dog_name(name=input("Enter a dog name: ")):
    return name


# 3 - more decorator practice
def decorator_func(initial_func):
    def wrapper_func():
        print(f"{initial_func()} soup")
    return wrapper_func()


@decorator_func
def ingredient():
    return "Onion"


# 4 - more decorator practice
def decorator_function(initial_function):
    def wrapper_function():
        print("Wrapper function picked some....")
        return initial_function()
    return wrapper_function()


@decorator_function
def prettify():
    print("..flowers for you")






