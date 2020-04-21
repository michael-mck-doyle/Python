'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''


class simple_Arithmetic():

    def add(x, y):
        '''Add function'''
        x = int(input("Enter a number: "))
        return x + y

    def subtract(x, y):
        '''Subtract function'''
        y = int(input("Enter a number: "))
        return x - y
