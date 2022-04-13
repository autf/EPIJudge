from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # assert x >= 0 # fails

    a = bytearray()
    if neg := x < 0:
        x = -x
    while x:
        x, d = divmod(x, 10) # divmod(-21, 10) -> (-2, 1)
        a.append(0x30+d)
    if neg:
        # a.append(b'-') # elt type of bytearray is integer! not byte
        a.append(ord('-'))
    a.reverse()
    v = a.decode()
    return a.decode() if a else '0'


def string_to_int(s: str) -> int:
    s0 = s[0]
    if not s0.isdigit():
        s = s[1:]
    v = 0
    for x in s:
        v = 10*v + (ord(x) & 0xf) # (.) needed
    return -v if s0 == '-' else v


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
