#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
LastDigit = number % 10 if number >= 0 else -(-number % 10)
print(f"Last digit of {number} is {LastDigit}",end=" ")
if LastDigit > 5:
    print("and is greater than 5")
elif LastDigit == 0:
    print ("and is 0")
else:
    print("and is less than 6 and not 0")
