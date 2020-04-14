'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

x = input("Enter a number between 1 and 1,000,000: ")
z = int(x)
y = 0
while y <= z:
    if y == z:
        print("The value entered is ", y)
        break
    print(y)
    y += 1


