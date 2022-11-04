"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.
"""

less_than_liter_container = float(input("Enter the amount of containers holding one liter or less: "))
more_than_liter_container = float(input("Enter the amount of containers holding more than one liter: "))
refund = (less_than_liter_container * 0.10) + (more_than_liter_container * 0.25)
print(f"Your total refund for returning the containers is ${refund:.2f}")
