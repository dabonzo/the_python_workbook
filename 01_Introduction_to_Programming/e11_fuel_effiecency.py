"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""
ONE_MPG_PER_MILE = 235.215
mpg = float(input("Enter miles per gallon: "))
print(f"{mpg} mpg is {ONE_MPG_PER_MILE / mpg:.2f} l/100km")
