"""
In this exercise you will reverse the process described in Exercise 24. Develop a
program that begins by reading a number of seconds from the user. Then your program
should display the equivalent amount of time in the form D:HH:MM:SS, where D,
HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours,
minutes and seconds should all be formatted so that they occupy exactly two digits.
Use your research skills determine what additional character needs to be included in
the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width.
"""
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

total_seconds = int(input("Enter the number of total seconds: "))
days = total_seconds // SECONDS_IN_DAY
total_seconds = total_seconds % SECONDS_IN_DAY
hours = total_seconds // SECONDS_IN_HOUR
total_seconds = total_seconds % SECONDS_IN_HOUR
minutes = total_seconds // SECONDS_IN_MINUTE
seconds = total_seconds % SECONDS_IN_MINUTE

print(f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}")
