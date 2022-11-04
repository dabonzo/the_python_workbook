"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.

A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
because one side of the coin has a loon (a type of bird) on it. The two dollar
coin, referred to as a toonie, was introduced 9 years later. It’s name is derived
from the combination of the number two and the name of the loonie.
"""

CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

cents = int(input("Enter the number in cents: "))

print(f"{cents // CENTS_PER_TOONIE} toonies")
# modulo operation to determine the rest of cents
cents = cents % CENTS_PER_TOONIE

print(f"{cents // CENTS_PER_LOONIE} loonies")
cents = cents % CENTS_PER_LOONIE

print(f"{cents // CENTS_PER_QUARTER} quarters")
cents = cents % CENTS_PER_QUARTER

print(f"{cents // CENTS_PER_DIME} dimes")
cents = cents % CENTS_PER_DIME

print(f"{cents // CENTS_PER_NICKEL} nickels")
cents = cents % CENTS_PER_NICKEL

print(f"{cents} pennies")
