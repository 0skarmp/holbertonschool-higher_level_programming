#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastn = number % 10
if number < 0:
    lastn = (-number) % 10
    lastn = -lastn
if number % 10 > 5:
    print(f"Last digit of {number} is {lastn} and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number} is {lastn} and is 0")
elif number % 10 < 6:
    print(f"Last digit of {number} is {lastn} and is less than 6 and not 0")
