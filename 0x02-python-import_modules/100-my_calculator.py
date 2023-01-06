#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        num_1 = int(sys.argv[1])
        num_2 = int(sys.argv[3])
        opp = operators[sys.argv[2]](num_1, num_2)
        print(f"{num_1} {sys.argv[2]} {num_2} = {opp}")
