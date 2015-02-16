__author__ = 'valthonis'


def majority_element(num):
    groups = {}
    for elem in num:
        if elem in groups:
            groups[elem] += 1
        else:
            groups[elem] = 1
    maxnum = 0
    maxkey = 0
    for i in groups:
        if maxnum < groups[i]:
            maxnum = groups[i]
            maxkey = i
    return maxkey
