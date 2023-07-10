#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastN = number % 10
if number < 0;
lastN = (-number) % 10
lastN = -lastN
if number % 10 > 5:
    print(f"Last digit of {number:d} is {lastN} and is greater than 5 ")
elif number % 10 == 0:
    print(f"Last digit of {number:d} is {lastN} and is 0 ")
elif number % 10 < 6:
    print(f"Last digit of {number:d} is {lastN} and is less than 6 and not 0 ")
