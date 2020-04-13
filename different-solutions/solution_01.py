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

#while we still have values in the unsorted list
while len(unsorted_list) > 0:
    #loop through the unsorted list to find the minimum value
    current_value = unsorted_list[0][1]
    min_value = unsorted_list[0][1]
    index = 0
    for tuple_ in unsorted_list:
        #save the minimum value to use outside of this for loop
        if tuple_[1] <= min_value:
            min_value = tuple_[1]
            min_index = index
        index += 1

    #push the minimum value onto the sorted list
    # The pop() method removes the item at the given index from the list and returns the removed item
    # By removing the lowest value during each loop and appending it to the sorted list in sequence of lowest first
    # then the items are added in ascending sequence
    sorted_list.append(unsorted_list.pop(min_index))
    print("unsorted list is " + str(unsorted_list))

print(sorted_list)

end_time = time.time()
print()
print()
print("Total execution time: {} seconds".format(end_time - start_time))
