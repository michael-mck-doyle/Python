'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

'''

# dictionary >>> list >>> tuples

from operator import itemgetter, attrgetter

my_dict = {"emily": 12, "zax": 23, "mia": 13, "jeremiah": 4, "russel": 15}
my_tuples_list = my_dict.items()
print(my_tuples_list)
print()
# enter either 0, 1, 2...etc...for the key itemgetter...the list will then be sorted based on the entry value
my_tuples_list = sorted(my_tuples_list, key=itemgetter(0))
print("my_tuples_list: ", my_tuples_list)
print()
second_tuples_list = sorted(my_dict, key=lambda name: name[0])
print("second_tuples_list: ", second_tuples_list)
