# Author - Renee Guldi
# SDEV140 - MJovanovich
# October 30, 2023
# This program will accept three integers via user input then output them in order 
# through decision statements

# this step will allow the user to input their three integers
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter your third number: "))
# this is where the program will locate the smallest number

if x <= y and x <= z:
    small = x
    if y <= z:
        middle = y
        large = z
    else: 
        middle = z
        large = y
elif y <= x and y <= z:
    small = y
    if x <= z:
        middle = x
        large = z
    else: 
        middle = z
        large = x
else:
    small = z
    if x <= y:
        middle = x
        large = y
    else:
        middle = y
        large = z
print("Here is your chosen numbers in rising order: ", small, middle, large)