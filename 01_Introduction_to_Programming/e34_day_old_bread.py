"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. Each of
these amounts should be displayed on its own line with an appropriate label. All of
the values should be displayed using two decimal places, and the decimal points in
all of the numbers should be aligned when reasonable values are entered by the user.
"""
PRICE_OF_BREAD = 3.49
number_of_day_old_breads = int(input("Enter the number of loaves of day old bread: "))
regular_price = number_of_day_old_breads * PRICE_OF_BREAD
discount = regular_price * 0.6
total = regular_price - discount
print(f"Regular price of bread:{regular_price:15.2f}")
print(f"Discount:{discount:29.2f}")
print(f"Total for {number_of_day_old_breads} day old breads:{total:10.2f}")
