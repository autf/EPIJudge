from test_framework import generic_test


def square_root(k: int) -> int:
    # assert k >= 0 #-> true for all
    i = 0
    j = k
    while i < j:
        h = (i + j) // 2
        # ± 1 to escape inf loop when h == i or h == j
        if h * h <= k:
            i = h + 1
        else:
            j = h - 1
    return i if i * i <= k else i - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
