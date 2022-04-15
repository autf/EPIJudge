from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    d = {}
    m = float('inf')
    for i, x in enumerate(paragraph):
        try:
            m = min(m, i-d[x])
        except:
            pass
        finally:
            d[x] = i
    return m if m != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
