from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    from itertools import product
    m = [      '0',
          '1','ABC','DEF',
        'GHI','JKL','MNO',
       'PQRS','TUV','WXYZ']
    return [''.join(xs) for xs in product(*map(m.__getitem__, map(int, phone_number)))]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
