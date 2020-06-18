

'''
Operator	Meaning	                                                Example	        Result
and	        True if both booleans are True	                        True and True	True
or	        True if either of the operands is True	                True or False	True
not	        True if the boolean is false, False if boolean is true	not False	    True

'''


a, b, c = 5, 5, 10

# The 'and' operator means that each condition must be True for the overall condition to be True
print("\nLogical 'and' Operator")
print(a == b and c == 10)  # True and True = True
print(a == b and a == c)  # True and False = False

# The 'or' operator means that at least one of the conditions must be True for the overall condition to be True
print("\nLogical 'or' Operator")
print(a == b or a == c)  # True and False = True
print(a == c or b == c)  # False and False = False

# The 'not' operator simply means the opposite of the logical expression's value
print("\nLogical 'not' Operator")
print(a == b)  # not False = True
print(not a == b)  # not True = False




