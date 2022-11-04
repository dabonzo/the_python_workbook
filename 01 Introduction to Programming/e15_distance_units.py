"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""
INCHES_IN_FOOT = 12
FEET_IN_YARD = 3
FEET_IN_MILE = 5280


feet = int(input("Enter the number of feet: "))
print(f"{feet} feet are {feet * INCHES_IN_FOOT} inches")
print(f"{feet} feet are {feet / FEET_IN_YARD:.2f} yards")
print(f"{feet} feet are {feet / FEET_IN_MILE:.2f} miles")
