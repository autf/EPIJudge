from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def inrange(t, lo, hi):
        if not t:
            return True
        v = t.data
        # print(lo, v, hi)
        if not (lo <= v <= hi):
            return False
        return inrange(t.left, lo, v) and inrange(t.right, v, hi)
    inf = float('inf')
    return inrange(tree, -inf, inf)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
