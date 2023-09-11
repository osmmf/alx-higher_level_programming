#!/usr/bin/env python3
def no_c(my_string):
    rtrn = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            rtrn += my_string[i]
    return rtrn
