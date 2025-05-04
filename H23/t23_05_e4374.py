def read():
    n, m = map(int, input().split())
    edges = [None]
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    k = int(input())
    queries = []
    for _ in range(k):
        parts = list(map(int, input().split()))
        queries.append(parts[1:])
    return n, m, edges, queries

class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.r[x] < self.r[y]:
            self.p[x] = y
        else:
            self.p[y] = x
            if self.r[x] == self.r[y]:
                self.r[x] += 1

def tr(n, m, edges, removed_edges):
    dsu = DSU(n)
    removed = set(removed_edges)
    for i in range(1, m + 1):
        if i not in removed:
            a, b = edges[i]
            dsu.unite(a, b)
    root = dsu.find(1)
    for i in range(2, n + 1):
        if dsu.find(i) != root:
            return False
    return True


n, m, edges, queries = read()
for q in queries:
    print("Connected" if tr(n, m, edges, q) else "Disconnected")