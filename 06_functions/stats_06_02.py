'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

from random import randrange


def ran_list():
    x = 0
    my_num_list = []
    while x < 20:
        y = (randrange(1, 100))
        my_num_list.append(y)
        x += 1
    return my_num_list


r = ran_list()
# print(r)


def stats(r):
    a = max(r)
    b = min(r)
    c = sum(r)/len(r)
    d = sum(r)
    return a, b, c, d


print(r)
val_returned = list(stats(r))
print(type(val_returned))
print(val_returned)
max_val = val_returned[0]
print("max value: ", max_val)
min_val = val_returned[1]
print("min value: ", min_val)
avge_val = val_returned[2]
print("average value: ", avge_val)
sum_val = val_returned[3]
print("sum: ", sum_val)
