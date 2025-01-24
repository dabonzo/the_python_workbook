"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
"""

# Constants
INTEREST_IN_PERCENT = 4

# Input: Initial deposit
balance = float(input("How much money do you want to deposit into the account: "))

# Calculate balance after 1st, 2nd, and 3rd years
balance = balance + (balance * (INTEREST_IN_PERCENT / 100))  # After 1st year
balance_after_first_year = balance

balance = balance + (balance * (INTEREST_IN_PERCENT / 100))  # After 2nd year
balance_after_second_year = balance

balance = balance + (balance * (INTEREST_IN_PERCENT / 100))  # After 3rd year
balance_after_third_year = balance

# Output the results
print(f"""
Balance after first year:     {balance_after_first_year:.2f}
Balance after second year:    {balance_after_second_year:.2f}
Balance after third year:     {balance_after_third_year:.2f}
""")

