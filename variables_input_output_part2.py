# Author: Renee Guldi
# SDEV 140 - MJovanovich
# This program will ask for a score out of 15, then convert that score
# to a percentage. 
maxScore = 15
#
userInput = int(input("Enter your score out of 15: "))
#
if userInput > 15:
    userInput = 15
#
percentage = (userInput / maxScore) 
#
print("Here is your final grade percentage: ", percentage, "%")