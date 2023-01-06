#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 0
    if len(sys.argv[1:]) == 0:
        print("{:d} arguments.".format(len(sys.argv[1:])))
    elif len(sys.argv[1:]) == 1:
        print("{:d} argument:".format(len(sys.argv[1:])))
        for i in sys.argv[1:]:
            j += 1
            print("{:d}: {:s}".format(j, i))
    else:
        print("{:d} arguments:".format(len(sys.argv[1:])))
        for i in sys.argv[1:]:
            j += 1
            print("{:d}: {:s}".format(j, i))
