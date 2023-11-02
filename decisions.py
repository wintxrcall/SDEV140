# Author : Renee Guldi
# SDEV140 - MPJovanovich
# November 1, 2023
# This Python Program will accept four inputs of values from the user
# as coordinates, and be used in calculation of the distance between the 
# coordinates, then round them to the second decimal point.
import math
def main():
    ()

# This section will collect the coordinates from the user
   
x1 = int(input("Please enter your first X coordinate: "))
y1 = int(input("Please enter your first Y coordinate: "))
x2 = int(input("Please enter your second X coordinate: "))
y2 = int(input("Please enter your second Y coordinate: "))

# calculating the distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# calculating the rounded 2 decimal point distance
roundDistance = round(distance, 2)

# this will output the calculated variable
print("This is the distance between the two coordinates: ", roundDistance )