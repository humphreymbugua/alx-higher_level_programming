#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for i in matrix:
            num = 0
            for j in i:
                num += 1
                if num == len(i):
                    print("{:d}".format(j), end="")
                else:
                    print("{:d} ".format(j), end="")
            print()
