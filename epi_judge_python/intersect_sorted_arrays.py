from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    from itertools import groupby
    w = []
    i = 0
    for b, _ in groupby(B):
        try:
            while A[i] < b:
                i += 1
            if A[i] == b:
                w.append(b)
        except:
            break
    return w


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
