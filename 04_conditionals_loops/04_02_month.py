'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

month = input("Enter a number between 1 - 12, corresponding to a month: ")
x = int(month)
if x == 1:
    print("The month is January")
elif x == 2:
    print("The month is February")
elif x == 3:
    print("The month is March")
elif x == 4:
    print("The month is April")
elif x == 5:
    print("The month is May")
elif x == 6:
    print("The month is June")
elif x == 7:
    print("The month is July")
elif x == 8:
    print("The month is August")
elif x == 9:
    print("The month is September")
elif x == 10:
    print("The month is October")
elif x == 11:
    print("The month is November")
elif x == 12:
    print("The month is December")
else:
    print("Your number does not correspond to a month.")

print("Done")