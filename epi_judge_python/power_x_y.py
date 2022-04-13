from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - better method?
    a = 1.
    for _ in range(abs(y)):
        a *= x
    return a if y >= 0 else 1/a


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
