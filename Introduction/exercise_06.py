"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all the values
are displayed using two decimal places.
"""

# Constants
TAX_PERCENT = 25  # Tax rate in percentage
TIP_PERCENT = 18  # Tip rate in percentage

# Input: Cost of the meal
meal = float(input("Enter the cost of the meal (in your local currency): "))

# Calculations
tip = meal * (TIP_PERCENT / 100)          # Calculate the tip as 18% of the meal cost
tax = meal * (TAX_PERCENT / 100)          # Calculate the tax as 25% of the meal cost
grand_total = meal + tip + tax            # Compute the total

# Output
print(f"""
Receipt:
Meal Cost:       ${meal:.2f}
Tip ({TIP_PERCENT}%):       ${tip:.2f}
Tax ({TAX_PERCENT}%):       ${tax:.2f}
---------------------------
Grand Total:     ${grand_total:.2f}
""")

