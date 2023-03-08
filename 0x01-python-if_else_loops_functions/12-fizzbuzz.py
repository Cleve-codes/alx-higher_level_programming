#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            print("fizz")
            if i & 5 == 0:
                print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print("{}".format(i))
