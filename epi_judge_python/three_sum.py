from test_framework import generic_test

def has_two_sum(A, total):
    left, right = 0, len(A) - 1
    while left <= right:
        if A[left] + A[right] == total:
            return True
        elif A[left] + A[right] < total:
            left += 1
        else:
            right -= 1
    return False


def has_three_sum(A, t):
    # TODO - you fill in here.
    A.sort()
    return any(has_two_sum(A, t - value) for value in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
