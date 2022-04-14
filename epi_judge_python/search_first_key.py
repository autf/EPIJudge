from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    from bisect import bisect_left
    i = bisect_left(A, k)
    try:
        if A[i] == k:
            return i
        return -1
    except:
        return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
