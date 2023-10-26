# Author: Renee Guldi
# SDEV 140 - MJovanovich
# This program will have the user enter their name and
# the year they were born before calculating their age
# based off the current year January 1st. 
import datetime
# get current year
currentYear = datetime.datetime.now().year
# collect user's name
personName = input("Please enter your name: ")
birthYear = input("Please enter the year you were born: ")
# calculate age
currentAge = int(currentYear -(int(birthYear)))
# display name and age
print(personName, " was born in ", birthYear, "As of January 1st of ", currentYear, personName, "is currently ", currentAge)

