'''
Write a script that demonstrates a try/except/else.

'''


try:
    x = int(input("Please enter something: "))
    print(x/2)

except TypeError as e:
    print("Your entry seems incorrect!", e)

else:
    print(f"You entered the value {x}.  Good choice!")


