#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Calculate the last digit by taking the absolute value of the number and using % 10
last_digit = abs(number) % 10
# Checks whether the sign is positive or negative
if number < 0:
    sign = "-"
elif number >= 0:
    sign = ""
# Determine the appropriate message based on the last digit
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"
print(f"Last digit of {number} is {sign}{last_digit} {message}")
