"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
 The sum of a and b
 The difference when b is subtracted from a
 The product of a and b
 The quotient when a is divided by b
 The remainder when a is divided by b
 The result of log10 a
 The result of a^b
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Sum of {num1} and {num2} is {num1 + num2}")
print(f"The difference when {num2} is subtracted from {num1} is {num2 - num1}")
print(f"The product of {num1} and {num2} is {num1 * num2}")
print(f"The quotient when {num1} is divided by {num2} is {num1 / num2}")
print(f"The remainder when {num1} is divided by {num2} is {num1 % num2}")
print(f"The result of log10({num1}) is {math.log10(num1)}")
print(f"The result of {num1}^{num2} is {math.pow(num1,num2)}")
