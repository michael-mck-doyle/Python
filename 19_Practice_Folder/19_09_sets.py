


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                 # fast membership testing

print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                 # unique letters in aa - b                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both


'''
Set Operations
A | B   - A.union(B) - Returns a set which is the union of sets A and B.
A |= B  - A.update(B) -	Adds all elements of list B to the set A.
A & B   - A.intersection(B)	- Returns a set which is the intersection of sets A and B.
A - B   - A.difference(B) - Returns the set difference of A and B (the elements included in A, but not included in B).
A -= B  - A.difference_update(B)	Removes all elements of B from the set A.
A < B	Equivalent to A <= B and A != B
A > B	Equivalent to A >= B and A != B
'''

