#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_numvarble = number % -10
elif number >= 0:
    last_numvarble = number % 10
if last_numvarble > 5:
    print(f"Last digit of {number} is {last_numvarble} and is greater than 5")
elif last_numvarble == 0:
    print(f"Last digit of {number} is {last_numvarble} and is 0")
else:
    print(f"Last digit of {number} is {last_numvarble} and is less than 6 and not 0")

