#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = abs(number) % 10
print(f"last digit of {number} is {LastDigit}",end=" ")
if LastDigit > 5:
    print("is greater than 5")
elif LastDigit == 0:
    print ("and is 0")
else :
    print("and less than 6 and not 0")   
