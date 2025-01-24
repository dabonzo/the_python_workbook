"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""

from math import pi

# Input: Radius and height of the cylinder
radius = float(input("Enter the radius of the cylinder (in units): "))
height = float(input("Enter the height of the cylinder (in units): "))

# Calculate the volume
volume_of_cylinder = pi * radius**2 * height

# Output: Display the results
print(f"""
Cylinder Calculation
---------------------
Radius: {radius:.1f} units
Height: {height:.1f} units

The volume of the cylinder is {volume_of_cylinder:.1f} cubic units.
""")
