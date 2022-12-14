"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""
feet = int(input("Enter number of feet: "))
inches = int(input("Enter number of inches: "))
print(f"{feet} feet,{inches} inches are {(feet * 12+ inches) * 2.54:.0f} cm")
