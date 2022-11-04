"""
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
"""
month = input("Type in the month: ")
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or \
        month == "October" or month == "December":
    days = 31
elif month == "February":
    days = "28 or 28"
else:
    days = 30

print(f'{month} has {days} days')
