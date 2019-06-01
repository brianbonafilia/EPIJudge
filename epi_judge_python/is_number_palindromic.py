from test_framework import generic_test
import math


def is_palindrome_number(x):
    if x < 10:
        return x >= 0
    left_index = 10 ** math.floor(math.log10(x))
    right_index = 10
    while left_index > 0:
        if x // left_index != x % right_index:
            return False
        x %= left_index
        x //= 10
        left_index /= 100
    return True

        
    


if __name__ == '__main__':
    is_palindrome_number(74447)
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
