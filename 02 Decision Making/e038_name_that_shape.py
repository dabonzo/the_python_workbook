"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

name = ""
nsides = int(input("Enter the number of sides: "))
if nsides == 3:
    name = "triangle"
elif nsides == 4:
    name = "quadrilateral"
elif nsides == 5:
    name = "pentagon"
elif nsides == 6:
    name = "hexagon"
elif nsides == 7:
    name = "heptagon"
elif nsides == 8:
    name = "octagon"
elif nsides == 9:
    name = "nonagon"
elif nsides == 10:
    name = "decagon"

if name == "":
    print("The number of sides is not supported")
else:
    print(f"A shape with {nsides} sides is called a {name}")