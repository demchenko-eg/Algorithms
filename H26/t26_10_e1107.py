class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True

def kruskal(n, edges, skip_edge=None):
    dsu = DSU(n)
    total = 0
    count = 0
    for i, (w, u, v) in enumerate(edges):
        if i == skip_edge:
            continue
        if dsu.union(u, v):
            total += w
            count += 1
        if count == n - 1:
            break
    return total if count == n - 1 else float('inf')

n, m = map(int, input().split())
raw_edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    raw_edges.append((w, u, v))
edges = sorted(raw_edges)
mst_cost = 0
mst_edges = []
dsu = DSU(n)
for i, (w, u, v) in enumerate(edges):
    if dsu.union(u, v):
        mst_cost += w
        mst_edges.append((i, w, u, v))
    if len(mst_edges) == n - 1:
        break
second_mst_cost = float('inf')
for i, w, u, v in mst_edges:
    cost = kruskal(n, edges, skip_edge=i)
    second_mst_cost = min(second_mst_cost, cost)
print(mst_cost, second_mst_cost)