"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1) / 2
"""

number = int(input("Enter a positive integer: "))
sum_positive_numbers = (number * (number + 1)) // 2
print(f"The sum of the positive numbers for {number} is {sum_positive_numbers}")
