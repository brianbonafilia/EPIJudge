from test_framework import generic_test


def power(x, y):
    # because increases by the powers of two, and the fact that x to power of 
    # y where y = a + b, is equal to x to power a times x to the power b
    # we know that we can keep track of x to the power 2^n where n is the bit
    # index and if that bit is a 1 then we can multiply our result by x to the
    # power 2^n
    result, power = 1, y 
    if y < 0:
        power, x = -power, 1 / x
    while power:
        if power & 1:
            result *= x
        x = x * x
        power >>= 1
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
