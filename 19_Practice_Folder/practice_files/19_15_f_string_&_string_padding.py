

#f-strings
# the unfulfilling market vendor f-string example

food = ['apples', 'bananas', 'pears', 'pineapples', 'papayas', 'dragon fruit', 'guyabano' ]
num = int(input("Enter appetite on scale 1-10: "))

print(f"You'd like {num} {food[3]} ? Sorry, we only have {num-1}.")

print()
print()


# string padding

strng = "World"
print(f"Hello{strng: >50}")


strng = "Hello"
print(f"Hello{strng: >8}")

strng = "Hello"
print(f"Hello{strng: >0}")



