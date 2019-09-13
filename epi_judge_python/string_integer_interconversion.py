from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    if x == 0:
        return '0'
    chars = []
    negative = x < 0
    x = abs(x)
    while x != 0:
        chars.append(chr(ord('0') + x % 10))
        x //= 10
    if negative:
        chars.append('-')
    return ''.join(chars[::-1])


def string_to_int(s):
    # TODO - you fill in here.
    sum = 0
    multiplier = 1
    negative = False
    if s[0] == '-':
        negative = True
        s = s[1:]
    for char in reversed(s):
        sum += (ord(char) - ord('0')) * multiplier
        multiplier *= 10
    if negative:
        sum *= -1
    return sum


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
