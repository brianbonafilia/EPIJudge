from test_framework import generic_test

def plus_one(A):
    for i in reversed(range(0,len(A))):
        A[i] = A[i] + 1
        if A[i] != 10:
            break
        A[i] = 0
    if A[0] == 0:
        A[0] = 1
        A.append(0)
    return A


def plus_one_original(A):
    # TODO - you fill in here.
    carry = 1
    i = len(A) - 1
    while  i >= 0 and carry:
        carry = (A[i] + 1) // 10
        A[i] = (A[i] + 1) % 10
        i -= 1 
    if carry:
        A = [1] + A
    
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
