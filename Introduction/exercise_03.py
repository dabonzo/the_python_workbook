"""
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""

# Input: Read the width and length of the room
width = float(input("Enter the width of the room (in meters): "))
length = float(input("Enter the length of the room (in meters): "))

# Calculate the area
area = width * length

# Output: Display the area with proper formatting
print(f"The area of the room is {area:.2f} square meters.")
