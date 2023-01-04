#!/usr/bin/python3
string = ""
for i in range(122, 96, -1):
    if (i % 2 == 1):
        string += chr(i).upper()
    else:
        string += chr(i)
print("{}".format(string), end="")
