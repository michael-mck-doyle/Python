'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

"""
Reference for how to nest functions - https://stackoverflow.com/questions/6289646/python-function-as-a-function-argument

Yes. By including the function call in your input argument/s, you can call two (or more) functions at once.
For example:

def anotherfunc(inputarg1, inputarg2):
    pass
def myfunc(func = anotherfunc):
    print func
When you call myfunc, you do this:

myfunc(anotherfunc(inputarg1, inputarg2))
This will print the return value of anotherfunc.

Hope this helps!

"""
'''

# Solution 1
# a calls b
def a_func(b_func):
    return b_func + 1


# b calls c
def b_func(c_func):
    return c_func + 1


# c
def c_func(x):
    return x + 1


print(a_func(b_func(c_func(2))))


def house_sales(houses_sold, house_cost):
    return houses_sold * house_cost


def houses_sold(jan, feb, march):
    return jan + feb + march


def house_cost(cost):
    return cost


print("$ value of houses sold: $", house_sales(houses_sold(100, 200, 300), house_cost(5000)))

#example of type hinting
#def my_add(a: int, b: int) -> int:
 #   return a + b
