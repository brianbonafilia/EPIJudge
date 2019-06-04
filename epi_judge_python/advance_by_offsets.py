from test_framework import generic_test


def can_reach_end(A):
    # TODO - you fill in here.
    steps_can_take = 0
    i = 0
    while i < len(A) - 1:
        steps_can_take = max(steps_can_take - 1, A[i])
        if steps_can_take == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
