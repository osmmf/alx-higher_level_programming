#!/usr/bin/python3
if __name__ == "__main__":
    import sys 

    cnt = len(sys.argv) - 1
    if cnt == 0:
        print("0 arguments.")
    elif cnt == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(cnt))
    for x in range(cnt):
        print("{}: {}".format(x +1, sys.argv[x + 1]))
