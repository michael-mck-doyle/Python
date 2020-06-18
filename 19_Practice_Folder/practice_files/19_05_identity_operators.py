

'''

Operator	Meaning
is	        True if the variables on the left and right side of "is" point to the same object
is not	    True if the variables on the left and right side of "is not" do not point to the same object

'''

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # both have the same value
print(list1 is list2)  # but they are different objects in memory

'''
Generally, the above is what you should keep in mind. The comparison operator "=="
checks for same values, and the identity operator "is" checks for whether they are the same object.

However, for performance reasons, Python caches small numbers and strings (and tuples),
which might run you into a bit of a head-scratch-situation if you've never heard about it before.
example below
'''
print("For below examples, Python caches small immutable objects to improve performance.  These are not assigned to memory.")
num1 = 5
num2 = 5

print(num1 == num2)  # as expected, this returns True
print(num1 is num2)  # surprsingly this is True too because '5' is a small number and python caches it instead of allocating it to memory!!

# Python caches small immutable objects to improve performance

'''
Further References
https://www.journaldev.com/22925/python-id
https://wsvincent.com/python-wat-integer-cache/


'''