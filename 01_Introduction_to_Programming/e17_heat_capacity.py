"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT
Write a program that reads the mass of some water and the temperature change from
the user. Your program should display the total amount of energy that must be added
or removed to achieve the desired temperature change.

Hint: The specific heat capacity of water is 4.186 J/◦C . Because water has a
density of 1.0 grams per milliliter, you can use grams and milliliters inter-
changeably in this exercise.
Extend your program so that it also computes the cost of heating the water. Electricity is normally
billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use
your program to compute the cost of boiling the water needed for a cup of coffee.
Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.
"""
WATER_HEAT_CAPACITY = 4.186
ONE_JOULES_IN_KWH = 2.77778e-7
COST_PER_KWH = 0.089
mass_of_water = float(input("Enter the mass of the water (1ml = 1g): "))
temperature_change = float(input("Enter the temperature change in C: "))

energy = mass_of_water * WATER_HEAT_CAPACITY * temperature_change
print(
    f"The energy needed to increase {mass_of_water} ml water for {temperature_change} degrees celsius "
    f"is {energy} Joules")

cost = energy * ONE_JOULES_IN_KWH * COST_PER_KWH
print(
    f"The cost to increase {mass_of_water} ml water for {temperature_change} degrees celsius "
    f"is {cost} dollars")
