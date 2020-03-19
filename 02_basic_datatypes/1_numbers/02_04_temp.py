'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

temp_Farh = int(input("Please enter a temperature in Fahrenheit: "))

temp_C = (temp_Farh - 32) * (5 / 9)
temp_C = format(temp_C, '.2f')
#print(temp_C)


print (str(temp_Farh) + " degrees fahrenheit = " + str(temp_C) + " degrees Celsius")



