from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    ## [[middle speed]]
    # simulate ptr by array
    ls = [L1, L2]
    g = t = ListNode() # g for guardian, t for temp
    while all(ls):
        # lambda below is const, not newly build every loop
        # see bytecode via: https://godbolt.org/
        i = min(0, 1, key=lambda i: ls[i].data)
        x = ls[i]
        ls[i] = x.next
        t.next = t = x
    t.next = ls[0] or ls[1]
    return g.next

    ## [[fastest]]
    g = t = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            x = L1
            L1 = L1.next
        else:
            x = L2
            L2 = L2.next
        t.next = t = x
    t.next = L1 or L2
    return g.next

    ## [[slowest]]
    import heapq
    def each(l):
        while l:
            yield l.data
            l = l.next
    g = t = ListNode()
    for v in heapq.merge(each(L1), each(L2)):
        t.next = t = ListNode(v)
        # x = ListNode(v)
        # t.next = x
        # t = x
    return g.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
