"""
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:
area = (n*s*s) / (4 * tan(pi/n))
Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
"""
import math

side = float(input("Enter length of side of a regular polygon: "))
number = float(input("Enter number of sides of a regular polygon: "))

area = (number * side * side) / (4 * math.tan(math.pi/number))
print(f"The area of a regular polygon is {area:.2f}")