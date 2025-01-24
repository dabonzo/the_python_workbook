"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:

q = mCΔT.

Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Hint: The specific heat capacity of water is 4.186 J/g ◦ C . Because water has a den-
sity of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
in this exercise.
Extend your program so that it also computes the cost of heating the water. Elec-
tricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.

Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.
"""

# Constants
SPECIFIC_HEAT_CAPACITY = 4.186  # in J/g°C
ENERGY_COST_KWH_IN_CENTS = 8.9  # in cents per kilowatt-hour
JOULES_TO_KWH = 3600000  # Conversion factor: 1 kWh = 3,600,000 J

# Inputs
mass_of_water = float(input("Enter the mass of water (in grams): "))
start_temp = float(input("Enter the starting temperature (in °C): "))
end_temp = float(input("Enter the desired temperature (in °C): "))

# Energy and Cost Calculations
energy_in_joules = mass_of_water * SPECIFIC_HEAT_CAPACITY * (end_temp - start_temp)
energy_cost_in_cents = (energy_in_joules / JOULES_TO_KWH) * ENERGY_COST_KWH_IN_CENTS
energy_cost_in_dollars = energy_cost_in_cents / 100

# Coffee Calculation (250 ml of water from 20°C to 100°C)
coffee_mass = 250  # 250 ml of water = 250 grams
coffee_temp_change = 100 - 20  # From 20°C to 100°C
coffee_energy = coffee_mass * SPECIFIC_HEAT_CAPACITY * coffee_temp_change
coffee_cost_in_cents = (coffee_energy / JOULES_TO_KWH) * ENERGY_COST_KWH_IN_CENTS
coffee_cost_in_dollars = coffee_cost_in_cents / 100

# Output
print(f"""
The energy required to heat {mass_of_water} grams of water from {start_temp:.1f} °C to {end_temp:.1f} °C is {energy_in_joules:.2f} Joules.
The cost to heat that mass of water is ${energy_cost_in_dollars:.4f}.

The cost of boiling a cup of coffee (250 ml of water from 20°C to 100°C) is ${coffee_cost_in_dollars:.4f}.
""")
