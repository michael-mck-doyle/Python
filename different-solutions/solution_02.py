'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

# use to measure time of code execution
import time
start_time = time.time()
# your code

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

value_list = []
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

print(value_list)
value_list.sort() # value list is still a tuple - can it be sorted?

for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
            break

print(sorted_list)

# use to measure time of code execution
end_time = time.time()
print()
print()
print("Total execution time: {} seconds".format(end_time - start_time))
