#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    div = 10
elif number < 0:
    div = -10
mod_val = number % div
if mod_val > 5:
    print(f"Last digit of {number} is {mod_val} and is greater than 5")
elif mod_val == 0:
    print(f"Last digit of {number} is {mod_val} and is 0")
elif ((mod_val < 6) and ((mod_val) != 0)):
    print(f"Last digit of {number} is {mod_val} and is less than 6 and not 0")
