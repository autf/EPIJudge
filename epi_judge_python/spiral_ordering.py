from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    'just did same Q in LC today'
    a = []
    n = len(square_matrix)
    i = j = 0
    di, dj = 0, 1

    rt = lambda: (dj, -di)
    push = lambda: a.append(square_matrix[i][j])

    while n:
        n -= 1
        push()
        for _ in range(n):
            j += dj
            push()
        di, dj = rt()
        for _ in range(n):
            i += di
            push()
        di, dj = rt()
        j += dj
    return a


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
