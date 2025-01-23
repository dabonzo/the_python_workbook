"""
(Solved—12 Lines)
Write a program that reads a positive integer, n, from the user and then displays the
sum of all the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:

sum = ((n)(n + 1)) /2

"""

number = int(input("Enter a positive integer number n: "))
total_sum = number * (number + 1) // 2
print(f"""
sum = {number} * ({number} + 1) / 2

sum = {total_sum}
""")
("\n"
 "excercise\n"
 "\n")

