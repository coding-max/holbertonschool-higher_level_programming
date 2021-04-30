#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif argv[2] == '+':
        op = add
    elif argv[2] == '-':
        op = sub
    elif argv[2] == '*':
        op = mul
    elif argv[2] == '/':
        op = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = op(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(int(argv[1]), argv[2], int(argv[3]), result))
