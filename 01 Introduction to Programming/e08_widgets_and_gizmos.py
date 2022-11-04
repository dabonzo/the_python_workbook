"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts.
"""

GIZMO_WEIGTH = 112
WIDGET_WEIGTH = 75

number_of_widgets = int(input("Enter the number of widgets: "))
number_of_gizmos = int(input("Enter the number of gizmos: "))
total_weight = (number_of_widgets * WIDGET_WEIGTH) + (number_of_gizmos * GIZMO_WEIGTH)
print(
    f"The total weight of {number_of_widgets} widgets and {number_of_gizmos} gizmos is {total_weight} g or"
    f" {total_weight / 1000} kg")
