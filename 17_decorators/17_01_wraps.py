'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def say_hi():
    print("Hi.")

#hi = say_hi
#hi()

def say_moo():
    print("moooooooo!")


list_ = [say_hi, say_moo]

#print(list_[0])

#print(list_[0]())

list_ = [say_hi(), say_moo()]
print(list_)

# Decorator structure
def decorator_func(initial_func):
    def wrapper_func():
        return initial_func()
    return wrapper_func  # returns the wrapper func ready to be executed


# STEP ONE - SCOPES REVISIT
#def outer_func():
   # msg = "Weeeeeekend!"

   # def inner_func():
  #      print(msg)

 #   return inner_func

#say_wee = outer_func()
#say_wee()


def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func()


#say_woop = outer_func("woop-woop!")
#say_woop



# STEP THREE - AN EMPTY DECORATOR (PASSING A FUNCTION)

def decorator_func(initial_func):
    def wrapper_func():
        print("Wrapper function picked some....")
        return initial_func()
    return wrapper_func  # returns the wrapper func ready to be executed


@decorator_func
def prettify():
    print("flowers and stuff")

prettify()


#decorated_pretty = decorator_func(prettify)
#decorated_pretty()  # executes wrapper function which executes prettify() func
