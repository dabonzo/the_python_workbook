"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the Internet.
"""
celsius = float(input("Enter the temperature in degree Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15
print(f"{celsius} degree Celsius are {fahrenheit} degree Fahrenheit or {kelvin} degree Kelvin")
