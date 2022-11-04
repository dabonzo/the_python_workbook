"""
In this exercise you will create a program that reads a pressure from the user in kilo-
pascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""
pressure_in_kPa = float(input("Enter the pressure in kPa: "))
pressure_in_psi = pressure_in_kPa * 0.1450377377
pressure_in_bar = pressure_in_kPa / 100
pressure_in_atm = pressure_in_kPa / 101.325
print(f"Pressure in kPa: {pressure_in_kPa}")
print(f"Pressure in psi: {pressure_in_psi}")
print(f"Pressure in bar: {pressure_in_bar}")
print(f"Pressure in atm: {pressure_in_atm}")
