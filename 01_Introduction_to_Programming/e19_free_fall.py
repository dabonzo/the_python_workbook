"""
Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2 . You can use the formula vf = sqrt(vi^2 + 2ad) to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
"""
import math

ACCELERATION = 9.8
height = float(input("Enter the height in m from which an object is dropped: "))
start_speed = 0
final_speed = math.sqrt(start_speed * start_speed + (2 * ACCELERATION * height))
print(f"The final speed of an object dropped from {height} meters bey hitting the ground will be {final_speed} m/s")
