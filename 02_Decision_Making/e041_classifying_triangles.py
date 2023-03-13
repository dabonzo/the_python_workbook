"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the
user. Then display a message that states the triangle’s type.
"""

length_a = float(input("Enter a-side of a triangle: "))
length_b = float(input("Enter b-side of a triangle: "))
length_c = float(input("Enter c-side of a triangle: "))
print(f"{length_a = }", f"{length_b = }", f"{length_c = }")
if (length_a == length_b) and (length_b == length_c):
    print("Triangle is equilateral")
elif (length_a != length_b) and (length_b != length_c) and (length_a != length_c):
    print("Triangle is scalene")
else:
    print("Triangle is isosceles")
