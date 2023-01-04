#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    j = 0
    for i in str:
        j += 1
        if (n == j - 1):
            string += ""
        else:
            string += i
    return string
