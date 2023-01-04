#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        div = -10
    else:
        div = 10
    num_div = number % div
    if num_div < 0:
        print("{}".format(-num_div), end="")
        return (-num_div)
    else:
        print("{}".format(num_div), end="")
    return (num_div)
