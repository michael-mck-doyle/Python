'''

Move the code you previously wrote to calculate how many seconds are in a year into this file.
Then execute it as a script to see the output printed to your console.

'''


def sec_years():
    year = 1
    #print("years = " + str(year))
    days = 365
    #print("days = " + str(days))
    hours = 24
    #print("hours = " + str(hours))
    minutes = 60
    #print("minutes =" + str(minutes))
    seconds = 60
    #print("seconds =" + str(seconds))
    numberofseconds = year * days * hours * minutes * seconds
    #print ("The number of seconds in a year is: " + str(numberofseconds))
    return numberofseconds

x = sec_years()
print(x)

