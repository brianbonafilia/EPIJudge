import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    left, middle, right = 0, 0, len(A) - 1
    pivot = A[pivot_index]
    while middle <= right:
        if A[middle] < pivot:
            A[middle], A[left] = A[left], A[middle]
            left += 1
            middle += 1
        elif A[middle] == pivot:
            middle += 1
        else:
            A[middle], A[right] = A[right], A[middle]
            right -= 1
        

def dutch_flag_partition_first_solution(pivot_index, A):
    # TODO - you fill in here.
    i = 0
    j = len(A) - 1
    pivot = A[pivot_index]
    while i <= j:
        if A[i] < pivot:
            i += 1
        else:
            A[i], A[j] = A[j], A[i]
            j -= 1
    j = len(A) - 1
    while j >= i:
        if A[j] > pivot:
            j -= 1
        else:
            A[i], A[j] = A[j], A[i]
            i += 1




@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    dutch_flag_partition(5, [0, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0])
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
