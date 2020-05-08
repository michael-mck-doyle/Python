'''
Using list comprehension, create a list that contains the individual
letters using the word "CodingNomads".

For example:

word = "CodingNomads"
..your code
result_list = ['C', 'o', 'd', 'i', 'n', 'g', 'N', 'o', 'm', 'a', 'd', 's']

'''

word = "CodingNomads"
word_list = [i for i in word]
print(word_list)


#List comprehension examples
numbers = [i for i in range(10, 20)]
number_list = [x for x in range(20)]
print(numbers)
print(number_list)

