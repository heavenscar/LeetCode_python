__author__ = 'valthonis'


def isvalid(s):

    stack = []

    pair = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in pair.values():
            stack.append(char)
        else:
            if not stack:
                return False
            if stack.pop() == pair[char]:
                continue
            else:
                return False

    if not stack:
        return True
    else:
        return False


if __name__ == "__main__":
    assert isvalid("") is True
    assert isvalid("()") is True
    assert isvalid(")(") is False
    assert isvalid("([)]") is False
    assert isvalid("{}") is True
