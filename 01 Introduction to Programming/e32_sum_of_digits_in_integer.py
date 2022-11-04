"""
Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3 + 1 + 4 + 1 = 9.
"""
number = int(input("Enter a four digit integer: "))
digit_4 = number % 10
number = number // 10
digit_3 = number % 10
number = number // 10
digit_2 = number % 10
digit_1 = number // 10
summary = digit_1 + digit_2 + digit_3 + digit_4
print(f"The sum of {digit_1} + {digit_2} + {digit_3} + {digit_4} = {summary}")
