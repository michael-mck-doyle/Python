

'''

__ For....in.. __ statement

example taken from book, "A Byte of Python", "Control Flow" section - https://python.swaroopch.com/control_flow.html

The for..in statement is another looping statement which iterates over
a sequence of objects i.e. go through each item in a sequence. We will see more
about sequences in detail in later chapters. What you need to know right now
is that a sequence is just an ordered collection of items.

In this program, we are printing a sequence of numbers. We generate this sequence
of numbers using the built-in range function.
What we do here is supply it two numbers and range returns a sequence of numbers starting
from the first number and up to the second number.
For example, range(1,5) gives the sequence [1, 2, 3, 4]. By default, range takes a step count of 1.
If we supply a third number to range, then that becomes the step count. For example, range(1,5,2) gives [1,3].
Remember that the range extends up to the second number i.e. it does not include the second number.

Note that range() generates only one number at a time,
if you want the full list of numbers, call list() on the range(),
for example, list(range(5)) will result in [0, 1, 2, 3, 4]. Lists are explained in the data structures chapter.

'''




for i in range(1, 10):
    print(i - 1)
    print("hello next number")
else:
    print('The for loop is over')

print("next for loop __" * 3)
print()

# the 3rd number in the range i.e. 2, is the step sequence.  normally it is 1 but you can
# change this by using a 3rd number to indicate the step sequence
for i in range(1, 10, 2):
    print(i - 1)
    print("hello next number")
else:
    print('The for loop is over')

print("next for loop __" * 3)
print()
