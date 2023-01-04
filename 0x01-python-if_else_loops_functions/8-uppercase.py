#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if i in "abcdefghijklmnopqrstuvwxyz":
            num = ord(i) - 32
        else:
            num = ord(i)
        string += chr(num)
    print("{}".format(string))
