#!/usr/bin/python3
def fizzbuzz():
    value = ""
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            value += "FizzBuzz "
        elif (i % 5 == 0) and (i % 3 != 0):
            if (i != 100):
                value += "Buzz "
            else:
                value += "Buzz"
        elif (i % 5 != 0) and (i % 3 == 0):
            value += "Fizz "
        else:
            value += str(i) + " "
    print("{}".format(value), end=" ")
