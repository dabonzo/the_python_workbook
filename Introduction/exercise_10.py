"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a**b

Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
from math import log10

first_number = int(input("Enter the first integer (a): "))
second_number = int(input("Enter the first integer (b): "))


# Output: Perform and display calculations
print(f"""
The sum of a and b:                             {first_number + second_number}
The difference when b is subtracted from a:     {first_number - second_number}
The product of a and b:                         {first_number * second_number}
The quotient when a is divided by b:            {first_number / second_number}
The remainder when a is divided by b:           {first_number % second_number}
The result of log10 a:                          {log10(first_number):.2f}
The result of a**b:                             {first_number ** second_number}
""")

