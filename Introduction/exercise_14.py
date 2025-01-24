"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""

# Conversion constants
INCH_IN_CM = 2.54

# Input: Read feet and inches
feet = int(input("Enter the number of feet: "))
inches = int(input("Enter the number of inches: "))

# Calculate total inches and convert to centimeters
total_inches = feet * 12 + inches
total_centimeters = total_inches * INCH_IN_CM

# Output the result
print(f"{feet} feet and {inches} inches are equivalent to {total_centimeters:.2f} centimeters.")



