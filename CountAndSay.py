__author__ = 'valthonis'

import itertools


def countandsay(n):

    if n == 0:
        return None

    if n == 1:
        return '1'

    s = '1'

    result_list = [s, ]

    for i in range(n - 1):
        s = result_list.pop()
        result_list.append(''.join((str(len(list(g))) + k) for k, g in itertools.groupby(s)))

    return result_list.pop()


if __name__ == "__main__":

    assert countandsay(0) is None
    print countandsay(1)
    print countandsay(2)
    print countandsay(3)
    print countandsay(4)
    print countandsay(5)
    print countandsay(6)
    print countandsay(7)
    print countandsay(8)
