from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int: # redo q11.8
    A.sort()
    return A[-k]

    import heapq
    return heapq.nlargest(k, A)[-1]

    # too SLOW; especially #503
    import heapq
    def make(i, j):
        x = max(range(i, j), key=A.__getitem__)
        return -A[x], i, x, j
    h = [make(0, len(A))]
    for _ in range(k-1):
        _, i, x, j = heapq.heappop(h)
        if i < x:
            heapq.heappush(h, make(i, x))
        x += 1
        if x < j:
            heapq.heappush(h, make(x, j))
    return -h[0][0]


    # def idx_of_max(indices):
    #     return max(indices, key=A.__getitem__)

    # def dc(k, i, j):
    #     assert i < j
    #     # print(k, i, j)
    #     h = idx_of_max(range(i, j))
    #     print(k, (i, h), (h+1,j))
    #     # h = max(range(i, j), key=A.__getitem__)
    #     # print(k,(i,j),h)
    #     k //= 2
    #     if j - i == 1 or k == 0:
    #         return h
    #     if h == i:
    #         return dc(k, h+1, j)
    #     if h == j - 1:
    #         return dc(k, i, h)
    #     i = dc(k, i, h)
    #     j = dc(k, h+1, j)
    #     return idx_of_max((i, j))
    #     # return max(i, j, key=A.__getitem__)
    # return A[dc(k, 0, len(A))]


    # from functools import cache
    # @cache
    # def max_idx(i, j):
    #     assert i < j
    #     if j - i == 1:
    #         return i
    #     h = (i + j) // 2
    #     i = max_idx(i, h)
    #     j = max_idx(h, j)
    #     return max(i, j, key=lambda i: A[i])
    # i, j = 0, len(A)
    # for _ in range(k):
    #     h = max_idx(i, j)



    # def x(i, j):
    #     match j - i:
    #         case 0: return float('-inf')
    #         case 1: return A[i]
    #     h = (i + j) // 2
    #     return max(x(i, h), x(h, j))
    # i, j = 0, len(A)
    # # v = x(i, j)
    # for _ in range(k):
    #     h = (i + j) // 2
    #     v1 = x(i, h)
    #     v2 = x(h, j)
    #     if v1 < v2:
    #         v = v2
    #         j = h
    #     else:
    #         v = v1
    #         i = h
    # return v

        # v = max(v1, v2)
        # if v1
        # v = x(i, j)
        # if i == j:
        #     return float('-inf')




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
