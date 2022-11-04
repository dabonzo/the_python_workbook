"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

days = int(input("Enter the amount of days: "))
hours = int(input("Enter the amount of hours: "))
minutes = int(input("Enter the amount of minutes: "))
seconds = int(input("Enter the amount of seconds: "))

total_seconds = (days * SECONDS_IN_DAY) + (hours * SECONDS_IN_HOUR) + (minutes * SECONDS_IN_MINUTE) + seconds

print(f"Total seconds: {total_seconds}")
