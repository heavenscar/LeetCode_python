__author__ = 'valthonis'


def power(num, base):
    count = 0
    while num >= base:
        num = num / base
        count += 1
    return count


def excel(num):
    excess = num
    bitmap = []
    while excess >= 26:
        basepower = pow(26, power(excess, 26))
        bitmap.append(excess / basepower)
        excess %= basepower
        while basepower > 26 and excess < basepower/26:
            basepower /= 26
            bitmap.append(0)
    bitmap.append(excess)

    bitmap.reverse()
    length = len(bitmap)
    for i in range(length):
        if bitmap[i] == 0 and i != length-1:
            bitmap[i] = 26
            bitmap[i+1] -= 1
    bitmap.reverse()

    if bitmap[0] == 0:
        bitmap.pop(0)

    return ''.join(chr(i+64) for i in bitmap)


if __name__ == "__main__":
    assert power(32, 2) == 5
    assert power(1000, 10) == 3
    assert power(1007, 10) == 3
    print power(701, 26)

    assert excel(1) == 'A'
    assert excel(26) == 'Z'
    assert excel(27) == 'AA'
    assert excel(52) == 'AZ'

    print excel(701)
    print excel(702)
