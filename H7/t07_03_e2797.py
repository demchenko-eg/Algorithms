from math import sqrt

EMPTY = None

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

class Set:
    def __init__(self, size=23):
        self.size = size
        self.count = 0
        self.table = [EMPTY] * size

    def _hash(self, key, attempt):
        h1 = key % self.size
        h2 = 1 + (key % (self.size - 1))
        return (h1 + attempt * h2) % self.size

    def _rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2
        old_table = self.table
        self.table = [EMPTY] * self.size
        self.count = 0
        for key in old_table:
            if key is not EMPTY:
                self.set(key)

    def set(self, key):
        if self.size * 0.7 < self.count:
            self._rehash()
        attempt = 0
        while True:
            index = self._hash(key, attempt)
            if self.table[index] is EMPTY:
                self.table[index] = key
                self.count += 1
                return True
            elif self.table[index] == key:
                return False
            attempt += 1

    def contains(self, key):
        attempt = 0
        while True:
            index = self._hash(key, attempt)
            if self.table[index] is EMPTY:
                return False
            elif self.table[index] == key:
                return True
            attempt += 1


n = int(input())
numbers = map(int, input().split())
hash_set = Set()
unique_count = sum(hash_set.set(num) for num in numbers)
print(unique_count)
