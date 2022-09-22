#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = ['+', '-', '*', '/']
    for operator in ops:
        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        if operator == '-':
            print("{} + {} = {}".format(a, b, sub(a, b)))
        if operator == '*':
            print("{} + {} = {}".format(a, b, mul(a, b)))
        if operator == '/':
            print("{} + {} = {}".format(a, b, div(a, b)))
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
