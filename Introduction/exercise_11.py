"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""

CONVERSION_FACTOR = 235.214583

# Input: Fuel efficiency in MPG
miles_per_gallon = float(input("Enter the value for miles per gallon (MPG): "))

# Conversion calculation
l_per_100km = CONVERSION_FACTOR / miles_per_gallon

# Output: Show the result with units
print(f"{miles_per_gallon:.2f} miles per gallon is equivalent to {l_per_100km:.2f} liters per 100 kilometers.")


