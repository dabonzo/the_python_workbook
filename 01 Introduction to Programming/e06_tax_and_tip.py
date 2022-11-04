"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""

cost_of_meal = float(input("Enter the cost of the meal: "))
tip = cost_of_meal * 0.18
tax = cost_of_meal * 0.2
total_cost_of_meal = cost_of_meal + tax + tip
# 20.2f and 12.2f: the numbers 20 and 12 (spaces reserved for the left side of the decimal point)are used to align
# the price column: 12 for grand total is 8 characters less than the 20 spaces for tip and tax.
# That's because "Grand total: " has 8 characters more than "Tip: " or "Tax: "
# It's a little bit trial and error to get it right
print(f"Tip: {tip:20.2f}")
print(f"Tax: {tax:20.2f}")
print(f"Grand total: {total_cost_of_meal:12.2f}")
