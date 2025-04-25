class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.min_tree = [0] * (4 * self.n)
        self.max_tree = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.min_tree[node] = data[l]
            self.max_tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self.build(data, 2 * node, l, mid)
            self.build(data, 2 * node + 1, mid + 1, r)
            self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])
            self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])

    def update(self, node, l, r, idx, value):
        if l == r:
            self.min_tree[node] = value
            self.max_tree[node] = value
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node, l, mid, idx, value)
            else:
                self.update(2 * node + 1, mid + 1, r, idx, value)
            self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])
            self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if qr < l or ql > r:
            return (float('inf'), float('-inf'))
        if ql <= l and r <= qr:
            return (self.min_tree[node], self.max_tree[node])
        mid = (l + r) // 2
        left_min, left_max = self.query(2 * node, l, mid, ql, qr)
        right_min, right_max = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return (min(left_min, right_min), max(left_max, right_max))

n = 100000
a = [(i * i % 12345 + i * i * i % 23456) for i in range(1, n + 1)]
tree = SegmentTree(a)
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    if x > 0:
        res_min, res_max = tree.query(1, 0, n - 1, x - 1, y - 1)
        print(res_max - res_min)
    else:
        tree.update(1, 0, n - 1, -x - 1, y)