'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

# this solution has a lot less steps than the other four solutions.
# this solution only has 13 steps whereas the other solutions have 30+ steps
# compared to some other solutions this one executed almost twice as fast

import time
start_time = time.time()
# your code


unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

sorted_list = sorted(unsorted_list, key=lambda x: x[1])
print(sorted_list)


# use to measure time of code execution
end_time = time.time()
print()
print()
print("Total execution time: {} seconds".format(end_time - start_time))
