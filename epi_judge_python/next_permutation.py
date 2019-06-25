from test_framework import generic_test


def next_permutation(perm):
    # TODO - you fill in here.
    index = len(perm) - 2
    while index >= 0:
        if perm[index] < perm[index + 1]:
            swap_index = len(perm) - 1
            while perm[swap_index] <= perm[index]:
                swap_index -= 1
            perm[index], perm[swap_index] = perm[swap_index], perm[index]
            return perm[:index+1] + list(reversed(perm[index+1:]))
        index -= 1
    return [] 
            
                


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
