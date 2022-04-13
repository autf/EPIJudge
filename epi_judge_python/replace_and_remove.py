import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    j = len(s)
    for i in reversed(range(size)):
        x = s[i]
        if x != 'b':
            j -= 1
            s[j] = x

    def each():
        for i in range(j, len(s)):
            x = s[i]
            if x == 'a':
                yield 'd'
                yield 'd'
            else:
                yield x

    i = 0
    for x in each():
        s[i] = x
        i += 1
    return i


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
