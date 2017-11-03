#!/usr/bin/env python3
import operator
import readline
import sys
import colored
from colored import fg, bg, attr, stylize

ops = {
        '+': operator.add,
        '-': operator.sub,
        '^': operator.pow
}
grey = colored.fg("grey_54") 
blue = colored.fg("sky_blue_2")
green = colored.fg("pale_green_3b")
red = colored.fg("indian_red_1c")
orange = colored.fg("sandy_brown")

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1, arg2)
            stack.append(result)
    print(stylize("[", grey), end="")
    for val in stack:
        if val < 0 and val % 2 == 1:
            print(stylize(val, orange), ", ", end="")
        elif val < 0 and val % 2 != 1:
            print(stylize(val, red), ", ", end="")
        elif val >= 0 and val % 2 == 1:
            print(stylize(val, green), ", ", end="")
        else:
            print(stylize(val, blue), ", ", end="")
    print(stylize("]\n", grey), end="")
    return stack.pop()

def main():
    angry = colored.fg("red") + colored.attr("bold")
    print ('%s Hello World !!! %s' % (fg(1), attr(0)))
    print(stylize("This is VERY angry text.", angry, colored.attr("underlined")))
    print(stylize("This is green.", colored.fg("green")))
    while True:
        val = input("rpn calc> ")
        if val == 'q':
            return
        calculate(val)

if __name__ == '__main__':
    main()

