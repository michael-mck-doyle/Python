
'''

Keywords that are found in loops

break - 'break' ends the execution of the loop, skipping anything after
continue - 'continue' returns to the beginning of the loop, skipping anything after in that specific run.
 it starts the loop again with the next item.
pass - pass is used when code in a function has not been completed yet.  It allows the running of the program to continue.
It is mostly used as a placeholder while building out some functionality. It does effectively nothing - just allows the code to continue.



'''



my_list = [1, 2, 3, 4, 5]

# 'break' ends the execution of the loop, skipping anything after
for num in my_list:
  if num % 3 == 0:
    break
  print(num)
print("finished 'break' part")

print()
print()

# 'continue' returns to the beginning of the loop, skipping anything after in that specific run
# it starts the loop again with the next item
''' 
for num in my_list:
    if num % 3 == 0:
        continue
    print(num)
print("finished 'continue' part")
'''

print()
print()
'''
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
'''

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
    elif len(s) > 3:
        print("that should do it")
    continue
print('Input is of sufficient length')

