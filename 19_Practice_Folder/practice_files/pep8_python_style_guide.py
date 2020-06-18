'''

Reference
PEP 8 -- Style Guide for Python Code - https://www.python.org/dev/peps/pep-0008/
Control Flow, If, While, For... - https://python.swaroopch.com/control_flow.html

__Indentation__

Use 4 spaces per indentation level.

Notice that we use indentation levels to tell Python which statements belong to which block.
This is why indentation is so important in Python.
I hope you are sticking to the "consistent indentation" rule.


__ If statements __
Notice how the if statement contains a colon at the end
- we are indicating to Python that a block of statements follows
Note, this also applies to following "elif" and and "else" statements i.e. they should also be followed by a ':'

if guess == number:
elif guess < number:
else:

Remember that the elif and else parts are optional. A minimal valid if statement is:
if True:
    print('Yes, it is true')
'''

