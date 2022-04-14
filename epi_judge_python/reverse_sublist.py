from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    '1-based idx; start, finish inclusive. (book p.85)'
    # assert start <= finish
    if start == 0:
        return L

    g = t = ListNode(next=L)
    for _ in range(start-1):
        t = t.next
    eol = t
    w = []
    for _ in range(finish-start+1):
        t = t.next
        w.append(t)
    bor = t.next
    from itertools import pairwise
    for x, y in pairwise(w):
        y.next = x
    if w:
        eol.next = w[-1]
        w[0].next = bor
    return g.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
