#!/usr/bin/python3
def islower(c):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if ord(c) == ord(i):
            return True
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ord(c) == ord(i):
            return False
