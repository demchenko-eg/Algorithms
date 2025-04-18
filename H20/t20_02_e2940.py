class SegmentTree:
    def __init__(self, array):
        length = len(array)
        size = 1
        while size < length:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)
        for i in range(length):
            self.tree[size + i] = array[i]
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def add(self, pos, delta):
        i = pos + self.size
        self.tree[i] += delta
        i //= 2
        while i > 0:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def range_sum(self, left, right):
        res = 0
        l = left + self.size
        r = right + self.size
        while l <= r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if not (r & 1):
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res


n, q = map(int, input().split())
a = list(map(int, input().split()))
seg = SegmentTree(a)
results = []
for _ in range(q):
    parts = input().split()
    if parts[0] == '+':
        idx = int(parts[1]) - 1
        delta = int(parts[2])
        seg.add(idx, delta)
    else:
        l = int(parts[1]) - 1
        r = int(parts[2]) - 1
        results.append(str(seg.range_sum(l, r)))
print("\n".join(results))