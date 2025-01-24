"""
Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr**2. The
volume of a sphere is computed using the formula volume = 4/3 πr**3 .
"""

from math import pi

# Input: Radius
radius = float(input("Enter the radius: "))

# Calculations
area_circle = pi * radius**2
volume_sphere = (4 / 3) * pi * radius**3

# Output: Results
print(f"""
Radius: {radius}

Area of the circle   : {area_circle:.2f} square units
Volume of the sphere : {volume_sphere:.2f} cubic units
""")