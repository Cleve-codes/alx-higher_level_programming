#!/usr/bin/python3
import random
number = random.randint(-10, 10)
new_num = 0

if (number > 0):
    new_num = number
    print(f"{new_num} is positive")

elif (number == 0):
    print(f"{number} is zero")

elif (number < 0):
    new_num = number
    print(f"{new_num} is negative")
