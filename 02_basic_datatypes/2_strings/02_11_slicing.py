'''

Using string slicing, take in the user's name and print out their name translated,
moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
n = []
s = 0
while s < 3:
    name = (input("Please enter a name: "))
    x = name[0]
    y = name[1:]
    z = "ay"
    print(x, y, z)
    new_name = y + x + z
    n.append(new_name)
    print(new_name)
    s = s + 1


print(n)







