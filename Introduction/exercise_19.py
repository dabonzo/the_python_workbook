"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2 . You can use the formula vf = sqrt(vi**2 + 2ad) to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
"""
import math

# Constants
GRAVITATIONAL_ACCELERATION = 9.82  # in m/s^2
INITIAL_SPEED = 0  # in m/s

# Input: Height from which the object is dropped
distance = float(input("Enter the height from which the object is dropped (in meters): "))

# Calculate the final speed
final_speed = math.sqrt(INITIAL_SPEED**2 + 2 * GRAVITATIONAL_ACCELERATION * distance)

# Output: Display the results
print(f"""
Height from which the object is dropped: {distance:.2f} m
Final speed when it hits the ground     : {final_speed:.2f} m/s
""")