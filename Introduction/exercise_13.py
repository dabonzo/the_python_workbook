"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
A one dollar coin was introduced in Canada in 1987. It is referred to as a
loonie because one side of the coin has a loon (a type of bird) on it. The two
dollar coin, referred to as a toonie, was introduced 9 years later. Its name is
derived from the combination of the number two and the name of the loonie.
"""

# Coin values in cents
PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25
LOONIE = 100
TOONIE = 200

# Input: Amount in cents
amount_in_cents = int(input("Enter the amount in cents: "))

# Compute the number of each coin type
toonies = amount_in_cents // TOONIE
remaining_amount = amount_in_cents % TOONIE

loonies = remaining_amount // LOONIE
remaining_amount %= LOONIE

quarters = remaining_amount // QUARTER
remaining_amount %= QUARTER

dimes = remaining_amount // DIME
remaining_amount %= DIME

nickels = remaining_amount // NICKEL
remaining_amount %= NICKEL

pennies = remaining_amount // PENNY

# Output the results
print(f"""
Denominations of coins for {amount_in_cents} cents:
---------------------------------------------------
Toonies     : {toonies} coins
Loonies     : {loonies} coins
Quarters    : {quarters} coins
Dimes       : {dimes} coins
Nickels     : {nickels} coins
Pennies     : {pennies} coins
""")