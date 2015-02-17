__author__ = 'valthonis'

"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

# of course you can do this within one line: 
# def isPalindrome(x):
#     return str(x)[::-1] == str(x)

def isPalindrome(x):

    a = 0
    b = x
    while b > 0:
        b /= 10
        a += 1

    c = 0

    b = x
    while x > 0:
        c += ((x % 10) * pow(10, a-1))
        x /= 10
        a -= 1

    return c == b


if __name__ == "__main__":
    assert isPalindrome(121) is True
    assert isPalindrome(0) is True
    assert isPalindrome(12) is False
