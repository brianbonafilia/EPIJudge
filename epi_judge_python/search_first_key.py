from test_framework import generic_test


def search_first_of_k(A, k):
    # TODO - you fill in here.
    left, right, result = 0, len(A) - 1, -1
    while(left <= right):
        middle = (left + right) // 2
        if A[middle] < k:
            left = middle + 1
        elif A[middle] == k:
            result = middle
            right = middle - 1
        else:
            right = middle - 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
