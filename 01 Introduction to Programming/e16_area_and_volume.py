"""
Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr^2 . The
volume of a sphere is computed using the formula volume = (4/3)*πr^3 .
"""
import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * math.pow(radius, 2)
volume = (4 / 3) * math.pi * math.pow(radius, 3)
print(
    f"A circle with a radius of {radius} has an area of {area:.2f} and a sphere with the same radius has a volume of "
    f"{volume:.3f}")

