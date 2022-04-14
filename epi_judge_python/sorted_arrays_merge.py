from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    import heapq
    # return list(heapq.merge(*sorted_arrays))

    def make(it):
        it = iter(it)
        return next(it), id(it), it
    h = list(map(make, sorted_arrays))
    heapq.heapify(h)
    a = []
    while h:
        x, _, it = h[0]
        a.append(x)
        try:
            heapq.heapreplace(h, make(it))
        except:
            heapq.heappop(h)
    return a


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
