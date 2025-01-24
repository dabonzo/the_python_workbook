"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""

# Conversion constants
FEET_TO_INCHES = 12
YARDS_TO_FEET = 3
MILE_TO_FEET = 5280

# Input: Measurement in feet
feet = int(input("Enter the number of feet: "))

# Output: Converted distances
print(f"""
{feet} feet are equivalent to:
  {feet * FEET_TO_INCHES} inches,
  {feet / YARDS_TO_FEET:.2f} yards,
  {feet / MILE_TO_FEET:.4f} miles.
""")
