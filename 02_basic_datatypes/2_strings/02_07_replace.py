'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''


r = (input("Please enter a string of words: "))
s = (input("Please enter a symbol: "))
firstchar = r[0]

r = r.replace(firstchar, "*")

print(r)
print(s)

