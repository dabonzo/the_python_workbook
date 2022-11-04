"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
smallest_number = min(a, b, c)
largest_number = max(a, b, c)
middle_number = a + b + c - smallest_number - largest_number
print(f"The numers sorted are : {smallest_number, middle_number, largest_number}")
