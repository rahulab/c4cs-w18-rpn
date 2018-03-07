#!/usr/bin/env python 3

import operator
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.inv,
    '!': operator.mul,
}

prev = 0

def calculate(arg):
    global prev
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            if (token == '~'):
                arg2 = stack.pop()
                result = function(arg2)
            elif(token == '!'):
                arg2 = stack.pop()
                result = 1
                while (arg2 > 1):
                    result = function(result, arg2)
                    arg2 = arg2 - 1
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                try:
                    result = function(arg1, arg2)
                except ZeroDivisionError:
                    print('You tried to divide by zero :(')
                    result = prev
            prev = result
            stack.append(result)
        logger.debug(stack)
        print(stack)

    if (len(stack) != 1):
        raise TypeError

    return stack.pop()

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()