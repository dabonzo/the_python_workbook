"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in cm and the weight in kilograms then body mass index is
computed using the following formula:
BMI = (weight / height * height)
"""
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: ")) / 100
bmi = weight / (height * height)
print(f"Your BMI is {bmi:.2f}")
