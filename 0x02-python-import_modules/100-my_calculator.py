#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
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
    sys.argv[2] == ops[operator]
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
