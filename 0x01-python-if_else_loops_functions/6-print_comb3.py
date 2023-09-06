#!/usr/bin/python3
for x in range(10):
    for y in range(x, 10):
        if x < y:
            if x == 8 and y == 9:
                print("{:d}{:d}".format(x, y), end="\n")
            else:
                print("{:d}{:d}".format(x, y), end=", ")
