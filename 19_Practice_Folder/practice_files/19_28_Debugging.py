"""
__ References __

Breakpoint, PEP 553 -- Built-in breakpoint() - https://www.python.org/dev/peps/pep-0553/
There are many debuggers that can be used with Python, both on local machine and on remote machines.  Some examples below:
pdb — The Python Debugger - https://docs.python.org/3/library/pdb.html
web-pdb 1.5.3 - https://pypi.org/project/web-pdb/
pudb - https://pypi.org/project/pudb/, https://documen.tician.de/pudb/
Python 3.7’s new builtin breakpoint - https://hackernoon.com/python-3-7s-new-builtin-breakpoint-a-quick-tour-4f1aebc444c
How To Use the Python Debugger - https://www.digitalocean.com/community/tutorials/how-to-use-the-python-debugger
Pdb Commands - https://web.stanford.edu/class/physics91si/2013/handouts/Pdb_Commands.pdf
PdbDebugger Commands - https://docs.python.org/3/library/pdb.html#debugger-commands
Part 1. Debugging Python Code - https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html
"""

a = 0
b = 42
breakpoint()
a += b
breakpoint()
