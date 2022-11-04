"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
"""

width = float(input("Enter the width of the field in feet: "))
length = float(input("Enter the length of the room in feet: "))
area_in_acres = (width * length) / 43560
print(f"The area in acres is: {area_in_acres:.4f}")
