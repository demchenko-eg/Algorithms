class Heap:
    def __init__(self):
        self.a = []
    def push(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.a[p] <= self.a[i]:
                break
            self.a[p], self.a[i] = self.a[i], self.a[p]
            i = p
    def pop(self):
        n = len(self.a)
        if n == 0:
            return None
        res = self.a[0]
        self.a[0] = self.a[-1]
        self.a.pop()
        n -= 1
        i = 0
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            if l >= n:
                break
            j = l
            if r < n and self.a[r] < self.a[l]:
                j = r
            if self.a[j] >= self.a[i]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
        return res

try:
    while True:
        k, d = map(int, input().split())
        if k == 1:
            print(1)
            continue
        N = (k ** (d + 1) - 1) // (k - 1)
        fact = 1
        for i in range(2, N + 1):
            fact *= i
        h = Heap()
        for depth in range(d + 1):
            sz = (k ** (d - depth + 1) - 1) // (k - 1)
            for _ in range(k ** depth):
                h.push(sz)
        prod = 1
        x = h.pop()
        while x is not None:
            prod *= x
            x = h.pop()
        print(fact // prod)
except EOFError:
    pass