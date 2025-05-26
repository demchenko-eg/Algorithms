class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True

t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    edges = []
    target_edge = None
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        if (u == p and v == q) or (u == q and v == p):
            target_edge = (w, u, v)
    edges.sort()
    dsu = DSU(n)
    mst_edges = set()
    for w, u, v in edges:
        if dsu.union(u, v):
            mst_edges.add((min(u, v), max(u, v)))
    if (min(p, q), max(p, q)) in mst_edges:
        print("YES")
    else:
        print("NO")