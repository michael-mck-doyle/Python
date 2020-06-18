

'''
#def say_hi():
   # print("Hi.")

#hi = say_hi
#hi()

#def say_moo():
    #print("moooooooo!")


l#ist_ = [say_hi, say_moo]

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


@decorator_func # this takes the decorator_func function and applies it to the prettify function
def prettify():
    print("flowers and stuff")

prettify()


#decorated_pretty = decorator_func(prettify)
#decorated_pretty()  # executes wrapper function which executes prettify() func


# STEP FIVE - USE IT FOR MANY THINGS!  You can apply the same decorator to many functions
# Or to put it another way you can put many types of coffee through the coffee maker to return a cup of coffee


@decorator_func
def prettify():
    print("flowers for you")

@decorator_func
def feed():
    print("apples and potatoes")

@decorator_func
def wallpaper():
    print("new wallpaper")
prettify()
feed()
wallpaper()


'''


def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))

# Outputs <p>lorem ipsum, John dolor sit amet</p>




def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

