from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    min_heap = []
    iterators = [iter(x) for x in sorted_arrays]
    for i, it in enumerate(iterators):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    answer = []
    while len(min_heap) > 0:
        next_val, index = heapq.heappop(min_heap)
        answer.append(next_val)
        next_element = next(iterators[index], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, index))

    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
