from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    from functools import cache
    @cache
    def dp(i, j):
        if i <= 0:
            return max(0, j)
        if j <= 0:
            return i
        i -= 1
        j -= 1
        rm = 1 + min(dp(i+1,j), dp(i,j+1))
        tr = (A[i] != B[j]) + dp(i, j)
        return min(rm, tr)
    return dp(len(A), len(B))
    #     # if A[i] == B[j]:
    #     #     return dp(i, j)
    #     # return 1 + min(dp(i+1,j), dp(i,j+1))
    #     return (A[i] != B[j]) + min(dp(i,j), dp(i,j+1))
    #     # return min((A[i] != B[j]) + dp(i, j), dp(i+1, j), dp(i, j+1))
    #     # return (A[i] != B[j]) + dp(i, j)
    # # TODO - you fill in here.
    # assert dp(-1,-1) == 0
    # assert dp(-1,0) == 0
    # assert dp(-1,7) == 7
    # assert dp(0,-1) == 0
    # assert dp(7,-1) == 7
    # assert dp(0,4) == 4
    # assert dp(4,0) == 4

    # return dp(len(A), len(B))

    # # N = len(B)
    # # return min(dp(i, N) for i in range(len(A)))
    # # M = len(A)
    # # return min(dp(M, j) for j in range(len(B)+1))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
