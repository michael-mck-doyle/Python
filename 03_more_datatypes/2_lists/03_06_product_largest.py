'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

tally = []
nums_entered = 5
while len(tally) < nums_entered:
    item = input("Enter a number to the list: ")
    tally.append(item)

tally.sort()

print("The largest number in the list is: " + str(tally[4]))
print(tally)
