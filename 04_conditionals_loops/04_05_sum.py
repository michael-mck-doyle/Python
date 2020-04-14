'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

x = input("Enter a starting number: ")
y = input("Enter an ending number: ")
w = int(x)
z = int(y)
sum = 0

while w <= z:
    sum = sum + w
    print(sum)
    w += 1
print(sum)

