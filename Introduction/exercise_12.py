"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1 , g1 ) and (t2 , g2 ) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1 ) × sin(t2 ) + cos(t1 ) × cos(t2 ) × cos(g1 − g2 ))
The value 6371.01 in the previous equation wasn’t selected at random. It is
the average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
Hint: Python’s trigonometric functions operate in radians. As a result, you will
need to convert the user’s input from degrees to radians before computing the
distance with the formula discussed previously. The math module contains a
function named radians which converts from degrees to radians.
"""
from math import sin, cos, acos, radians

# Constant
AVERAGE_RADIUS_OF_EARTH = 6371.01  # in kilometers

# Input: Latitude and longitude of the first point
t1 = float(input("Enter latitude of the first point (in degrees, -90 to 90): "))
g1 = float(input("Enter longitude of the first point (in degrees, -180 to 180): "))
print("----------------------------------------------------------------")

# Input: Latitude and longitude of the second point
t2 = float(input("Enter latitude of the second point (in degrees, -90 to 90): "))
g2 = float(input("Enter longitude of the second point (in degrees, -180 to 180): "))

# Calculate the great-circle distance
distance = AVERAGE_RADIUS_OF_EARTH * acos(
    sin(radians(t1)) * sin(radians(t2)) +
    cos(radians(t1)) * cos(radians(t2)) * cos(radians(g1) - radians(g2))
)

# Output the results
print(f"""
The distance between:
    Point 1 (Latitude: {t1:.2f}, Longitude: {g1:.2f})
    Point 2 (Latitude: {t2:.2f}, Longitude: {g2:.2f})
is approximately {distance:.2f} kilometers.
""")
"""
Enter latitude of the first point on the Earth: 48.3069
Enter longitude of the first point on the Earth: 14.2859
----------------------------------------------------------------
Enter latitude of the second point on the Earth: 46.0533
Enter longitude of the second point on the Earth: 16.1783
"""