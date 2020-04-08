'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''

'''
Statistics module - https://docs.python.org/3/library/statistics.html?highlight=statistics#module-statistics
datetime — Basic date and time types - https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime

'''
from statistics import mean

data = [20, 40, 60]

print(mean(data))


import datetime

x = datetime.date(2020, 4, 7)
print(x)

y = datetime.date.today()
print(y)



