from test_framework import generic_test
from test_framework.test_failure import TestFailure


class _dll:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    # __repr__ = lambda self: str(self.val)
    def __repr__(self):
        return str(self.val)

    def rm(self):
        _dll.link(self.prev, self.next)

    def prepend(self, x):
        _dll.link(self.prev, x)
        _dll.link(x, self)

    @staticmethod
    def link(a, b):
        a.next = b
        b.prev = a


class LruCache:

    def __init__(self, capacity: int) -> None:
        self._cap = capacity
        self._m = {}
        g = _dll()
        g.prev = g.next = g
        self._g = g

    def lookup(self, isbn: int) -> int:
        # print(isbn, self._m)
        try:
            l = self._m[isbn]
        except:
            return -1
        else:
            l.rm()
            self._g.prepend(l)
            return l.val

    def insert(self, isbn: int, price: int) -> None:
        try:
            l = self._m[isbn]
            l.rm()
        except:
            if len(self._m) == self._cap:
                lru = self._g.next
                lru.rm()
                del self._m[lru.key]
            l = _dll(isbn, price)
            self._m[isbn] = l
        finally:
            self._g.prepend(l)

    def erase(self, isbn: int) -> bool:
        try:
            l = self._m[isbn]
        except:
            return False
        else:
            del self._m[isbn]
            l.rm()
            return True


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
