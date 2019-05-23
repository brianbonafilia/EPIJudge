from test_framework import generic_test


def count_bits(x):
    """ we can also create a cache """
    return 0

def count_bits_one_at_a_time(x):
    """ In order to count bits we can use the x & (x-1) trick"""
    count = 0
    while x:
        x = x & (x-1)
        count += 1

    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
