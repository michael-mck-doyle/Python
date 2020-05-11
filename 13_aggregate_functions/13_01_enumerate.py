'''
Demonstrate the use of the .enumerate() function.


builtins class enumerate(Iterator[Tuple[int, _T]], Generic[_T])
Return an enumerate object.

iterable
an object supporting iteration
The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
enumerate is useful for obtaining an indexed list:
(0, seq[0]), (1, seq[1]), (2, seq[2]), ...
  < Python 3.8 (labs) >
`enumerate(Iterator[Tuple[int, _T]], Generic[_T])` on docs.python.org

More details on enumerate function:
https://docs.python.org/3.8/library/functions.html#enumerate

Using enumerate function is equivalent to writing:
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

'''

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i, d in enumerate(days_of_the_week, start=1):
    print(f"{i} : {d}")


