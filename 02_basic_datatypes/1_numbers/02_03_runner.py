'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

import math

distance_miles = 10
distance_kilometres = distance_miles*1.6
minutes = 30
seconds = 30
time_hours = ((minutes*60)+seconds)/3600

print("running time is " + format(time_hours, '.2f') + " hours")

speed = distance_kilometres / time_hours

print("speed in km/hr = " +format(speed, '.2f'))





