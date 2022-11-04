"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places.
"""

deposit = float(input("Enter the amount of money you want to deposit: "))
amount_after_first_year = deposit * 1.04
amount_after_second_year = amount_after_first_year * 1.04
amount_after_third_year = amount_after_second_year * 1.04
print(f"Deposit: {deposit}")
print(f"After 1. year: {amount_after_first_year:8.2f}")
print(f"After 2. year: {amount_after_second_year:8.2f}")
print(f"After 3. year: {amount_after_third_year:8.2f}")
