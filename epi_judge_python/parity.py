from test_framework import generic_test


def parity(x: int) -> int:
    '''
    let x be as most 128 bit
    fold in half + xor
    '''
    assert x >= 0
    assert x < (1 << 128)
    k = 64
    while k:
        low = (1 << k) - 1
        x = (x >> k) ^ x & low
        k >>= 1
    return x


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
