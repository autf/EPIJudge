from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def height_et_balanced(t) -> (int, bool):
        if not t:
            return 0, True
        h1, ok = height_et_balanced(t.left)
        if not ok:
            return -1, False
        h2, ok = height_et_balanced(t.right)
        h = 1 + max(h1, h2)
        ok = ok and abs(h1-h2) <= 1
        return h, ok
    return height_et_balanced(tree)[1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
