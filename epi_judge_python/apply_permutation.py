from test_framework import generic_test


def apply_permutation(perm, A):
    # TODO - you fill in here.
    i = 0
    while i < len(A):
        if perm[i] != -1:
            perm_val = perm[i]
            A[i], A[perm_val] = A[perm_val], A[i]
            perm[i] = perm[perm_val]
            perm[perm_val] = -1
        else:
            i += 1
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
