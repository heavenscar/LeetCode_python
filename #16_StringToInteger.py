__author__ = 'valthonis'

"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.
"""

import string


def atoi(s):

    if not s:
        return 0

    possible = '+-0123456789'
    convert = []
    length = len(s)

    for i in range(length):
        if s[i] in string.whitespace:
            if not convert:
                continue
            else:
                break
        if s[i] not in possible:
            break
        if s[i] in '+-':
            if s[i+1] in string.digits:
                convert.append(s[i])
            else:
                break
        if s[i] in string.digits:
            convert.append(s[i])

    if not convert:
        return 0

    result = int(''.join(convert))

    if result > 2147483647L:
        return 2147483647
    elif result < -2147483648L:
        return -2147483648
    else:
        return result

if __name__ == "__main__":
    assert atoi('   010') == 10
    assert atoi('-1092badf') == -1092
    assert atoi('+1092') == 1092
    assert atoi('+-2') == 0
    assert atoi(' b11228552307') == 0
