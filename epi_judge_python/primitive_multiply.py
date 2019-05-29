from test_framework import generic_test

UNSIGNED_INT = 64

def multiply(x, y):
    sum = 0
    while x:
        if x & 1:
            sum = add(sum, y)
        y <<= 1
        x >>= 1
    return sum

def add(x, y):
    while x & y:
        temp = (x & y) << 1
        x = x ^ y
        y = temp
    return x ^ y

        



        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
