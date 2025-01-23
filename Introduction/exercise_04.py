"""
Create a program that reads the length and width of a farmer’s field from the user in
meters. Display the area of the field in acres.
1 acre = 4047m2
"""

# Conversion factor
ACRE_CONVERSION = 4047  # 1 acre = 4047 m²

# Input prompts with validation
field_length = int(input("Enter the length of the farmer's field (in meters): "))
field_width = int(input("Enter the width of the farmer's field (in meters): "))

# Calculate area in square meters and convert to acres
field_area_m2 = field_length * field_width
field_area_acres = field_area_m2 / ACRE_CONVERSION

# Display the result
print(f"The area of the field is {field_area_acres:.2f} acres.")



