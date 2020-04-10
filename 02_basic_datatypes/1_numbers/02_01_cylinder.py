'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
# import the pi function from math module

import math
#radius = 3.14
#height = 5


radius = int(input("Please enter a radius in centimeters: "))
height = int(input("Please enter a height in centimeters: "))
cylinder_volume = ((radius**2) * height)*math.pi

print ("cylinder_volume = " + str(cylinder_volume))


surface_area = (2 * math.pi * radius**2) + ((2 * math.pi * radius) * height)

print ("surface_area = " + str(surface_area))













