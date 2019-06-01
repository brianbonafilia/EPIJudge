from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.
    result = 0
    negative = 1
    if x < 0:
        x, negative = -x, -1
    while x:
        result = (result * 10) + (x % 10)
        x //= 10
    return result * negative


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
