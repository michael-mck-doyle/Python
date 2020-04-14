'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''
# increment variable m so that the number of '*' increases by one each time
# decrement variable n so that the while loop eventually exits
n = 5
m = 1
while n > 0:
    print('*'*m)
    m += 1
    n -= 1


