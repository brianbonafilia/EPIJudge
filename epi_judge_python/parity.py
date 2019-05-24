from test_framework import generic_test


def parity(x):
    """ 
    In order to solve this we will use the fact that the parity of
    can be calculate by repeatedly cutting the word in half and XOR with
    the two halfs.

    An example of why is if we consider an 8 bit example 10101101

    First you split it into 0101 1101 when XOR 
        1010
        1101
        -----
        0111

    Then you split it into 10 01 when you XOR this you get 11
        01
        11
        --
        10
    Finally you have 1 and 0 , you XOR this and get 0
        0
        1
        -
        1  
    Thus the answer is a parity of 1.
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x01



if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
