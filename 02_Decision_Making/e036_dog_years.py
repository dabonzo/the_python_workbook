"""
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
"""
DOG_HUMAN_YEARS_RELATION_TWO_YEARS_AND_LESS = 10.5
DOG_HUMAN_YEARS_RELATION_MORE_THAN_TWO_YEARS = 4.0

dog_years = float(input("Enter the dog years: "))
if dog_years <= 2:
    human_years = dog_years * DOG_HUMAN_YEARS_RELATION_TWO_YEARS_AND_LESS
else:
    human_years = (DOG_HUMAN_YEARS_RELATION_TWO_YEARS_AND_LESS * 2) + (
                dog_years - 2) * DOG_HUMAN_YEARS_RELATION_MORE_THAN_TWO_YEARS
print(f"{dog_years:.2f} dog years are {human_years:.2f}")
