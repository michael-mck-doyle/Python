

#f-strings
# the unfulfilling market vendor f-string example

food = ['apples', 'bananas', 'pears', 'pineapples', 'papayas', 'dragon fruit', 'guyabano' ]
num = int(input("Enter appetite on scale 1-10: "))

print(f"You'd like {num} {food[1]} ? Sorry, we only have {num-1}.")

print()
print()


# string padding

strng = "heiheo"
print(f"{strng: >3}")
