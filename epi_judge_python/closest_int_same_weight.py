from test_framework import generic_test


def closest_int_same_bit_count2(x):
    # TODO - you fill in here.
    UNSIGNED_INT = 63
    for i in range(0, UNSIGNED_INT):
        if(x >> i) & 1 != (x >> i + 1) & 1:
            x ^= (1 << i) | (1 << i + 1)
            return x
    return

def closest_int_same_bit_count(x):
    current_bit = 1
    if x & 1:
        current_bit <<= 1
        while current_bit & x:
            current_bit <<= 1
        x ^= current_bit
        current_bit >>= 1
        x ^= current_bit 
    else:
        current_bit <= 1
        while not current_bit & x:
            current_bit <<= 1
        x ^= current_bit
        current_bit >>= 1
        x ^= current_bit
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
