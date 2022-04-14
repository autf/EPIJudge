from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    from collections import deque
    q = deque()
    def push(x):
        if x: q.append(x)
    push(tree)
    q.append(None)
    a = []
    while q[0]:
        vs = []
        while x := q.popleft():
            vs.append(x.data)
            push(x.left)
            push(x.right)
        q.append(None)
        a.append(vs)
    return a

    a = []
    todo = [tree] if tree else []
    while todo:
        vs = []
        succ = []
        for x in todo:
            vs.append(x.data)
            if y := x.left: succ.append(y)
            if y := x.right: succ.append(y)
        todo = succ
        a.append(vs)
    return a


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
