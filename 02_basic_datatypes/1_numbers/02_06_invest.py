'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

import math

P = int(input("Please enter the amount of dollars you would like to invest: "))
r = float(input("Please enter the interest rate in decimal: "))
t = int(input("Please enter the number of years you would like to invest for: "))
n = int(input("Please enter the number of times interest is compounded each year e.g. monthly (12), quarterly (4) or yearly (1): "))

A = P*(1+r/n)**(n*t)
A = format(A, '.2f')
print("After " + str(t) + " years " + str(P) + " dollars will be worth " + str(A))



# A = the future value of the investment
# P = the principal investment amount
# r = the interest rate (decimal)
# n = the number of times that interest is compounded per period
# t = the number of periods the money is invested for

