__author__ = 'valthonis'


def compare_version(version1, version2):

    a = version1.split('.')
    b = version2.split('.')

    for i, j in zip(a, b):
        i = int(i)
        j = int(j)
        if i > j:
            return 1
        elif i < j:
            return -1
        else:
            continue

    lenA = len(a)
    lenB = len(b)

    if lenA == lenB:
        return 0

    if lenA > lenB:
        if sum(int(i) for i in a[lenB:]) > 0:
            return 1
    else:
        if sum(int(i) for i in b[lenA:]) > 0:
            return -1

    return 0


if __name__ == "__main__":
    assert compare_version('0.1', '0.2') == -1
    assert compare_version('01', '1') == 0
    assert compare_version('1.0', '1') == 0
