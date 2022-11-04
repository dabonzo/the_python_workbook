"""
Write a program that asks the user to enter the width and length of a room. Once
these values have been read, your program should compute and display the area of
the room. The length and the width will be entered as floating-point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""

width = float(input("Enter the width of the room in m: "))
length = float(input("Enter the length of the room in m: "))
# %.2f displays a floating point number with 2 decimal places
print("The are of the room is %.2f" % (width * length))
# output with f-strings
print(f"The are of the room is {width * length:.2f} square meters")
