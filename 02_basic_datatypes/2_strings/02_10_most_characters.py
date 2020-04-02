'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''


s = 0

list_string = []

while s < 3:
    r = (input("Please enter a string of words: "))

    list_string.append(r)

    s = s + 1

list_string.sort(key=len, reverse=True)

for x in list_string:
    print(len(x), ",", x)

print(list_string[0], " is the longest string entered.")


'''
- the code below are some of the other things i tried to come up with a solution
- this doesn't work because the max(list_string) below only considers the length
 of the first word in the string i think, not the total length of the string.  This is interesting because
 it highlights some of the test cases that can be carried out to check the code works under different conditions
 



max_len = (max(list_string))
print(max_len, " is the longest string.")
'''




'''
use loop
for x, y in thisdict.items():
  print(x, y)

#other stuff i tried
#print("days of the week include: ", list_string)
#list_dict = {}
#print(len(r), r)
    #x = len(r), r
    #print(x)
    #list_string.append(r)
#max_list_dict = max(list_dict, key=list_dict.get)
#print(max_list_dict)

#for max_len in list_dict:
   # print (max_len, list_dict[max_len])
'''