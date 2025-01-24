"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
"""

# Constants
WEIGHT_WIDGET = 75  # Weight of a widget in grams
WEIGHT_GIZMO = 112  # Weight of a gizmo in grams

# Input: Number of widgets and gizmos
number_of_widgets = int(input("Enter the number of widgets: "))
number_of_gizmos = int(input("Enter the number of gizmos: "))

# Calculate the total weight in grams
total_weight_grams = number_of_widgets * WEIGHT_WIDGET + number_of_gizmos * WEIGHT_GIZMO

# Optionally convert to kilograms
total_weight_kg = total_weight_grams / 1000

# Output the result
print(f"Total weight of the order: {total_weight_grams} grams ({total_weight_kg:.2f} kilograms)")




