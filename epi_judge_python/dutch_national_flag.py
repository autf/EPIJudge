import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    '''
    group elements eq pivot together, s.t.
        smaller be at left (if any)
        greater right
    use minimal swaps
    inplace

    #2ptr (3ptr)
    #invariant

    { x < p } , {[i] ? } , {[j] >= p } , {[k] > p }
        i is minimal idx of unkowns
        j is minimal idx of knowns s.t. A[j] >= p
        k is minimal idx of knowns s.t. A[k] > p
        (A[j:k] .== p)
    '''

    # A.sort() # ACC, and 5x faster than below!
    # return

    k = len(A)
    p = A[pivot_index]
    for x in reversed(A):
        if x <= p: break
        k -= 1
    assert k == len(A) or A[k] > p

    i = 0
    j = k
    while i < j:
        j -= 1
        x = A[j]
        if x > p:
            k -= 1
            A[j], A[k] = A[k], x
        elif x < p:
            A[i], A[j] = x, A[i]
            j += 1
            i += 1
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
