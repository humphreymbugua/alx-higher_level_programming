#!/usr/bin/python3
string = ""
for i in "abcdefghijklmnopqrstuvwxyz":
    if (i == 'e') or (i == 'q'):
        pass
    else:
        string += i
print("{}".format(string), end="")
