


'''
Create a python script that asks a user questions in the command line. The script should follow the outlined specs.

Specs
Receive the following arguments from the user:

kilometers to drive - datatype float
liters-per-kilometer usage of the car - datatype float - a rough guide is 13.0 litres/100 km for Honda CRV
price per liter of fuel - datatype float - depends on country but rough guide is $0.95 in the Philippines
Calculate the cost of the trip and display it to the user in the console.
'''

d = float(input("How many kilometers will you drive: "))
lpk = float(input("How many litres per kilometers does the car use: "))
ppl = float(input("What is the price of a liter of fuel: "))
cot = float(d*lpk*ppl)
print("The cost of your trip will be $" + format(cot, '.2f') + " dollars.")






