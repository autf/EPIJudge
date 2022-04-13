from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    m = '0123456789ABCDEF'

    a = 0
    neg = False
    x = num_as_string[0]
    if x not in m:
        neg = x == '-'
        num_as_string = num_as_string[1:]
    for x in num_as_string:
        a = b1 * a + m.index(x)

    b = bytearray()
    while a:
        a, i = divmod(a, b2)
        b.append(ord(m[i]))
    if neg:
        b.append(ord('-'))
    b.reverse()

    return b.decode() if b else '0'


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
