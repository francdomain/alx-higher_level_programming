#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    index = len(argv) - 1
    if index == 0:
        print("{} arguments.".format(index))
    elif index == 1:
        print("{} argument:".format(index))
    else:
        print("{} arguments:".format(index))
    for i in range(index):
        print("{}: {}".format(i + 1, argv[i + 1]))
