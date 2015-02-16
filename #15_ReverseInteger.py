__author__ = 'valthonis'

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


def reverse_interger(x):

    factor = -1 if x < 0 else 1

    num = str(abs(x))[::-1]

    result = factor * int(num)
    
    # in order to examine if the result is in the range of 32-bit int
    # in fact this judgement to prevent overflow is useless in python
    return result if -2147483648L < result < 2147483647L else 0
