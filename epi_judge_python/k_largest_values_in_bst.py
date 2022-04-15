from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def hcae(t):
        'hcae is reversed each'
        if not t:
            return
        yield from hcae(t.right)
        yield t.data
        yield from hcae(t.left)

    large = hcae(tree)
    return [next(large) for _ in range(k)]

    from itertools import islice
    return list(islice(hcae(tree), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
