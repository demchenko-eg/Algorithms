def bf(n, edges, source=1):
    INF = 30000
    dist = [INF] * (n + 1)
    dist[source] = 0
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    return dist[1:]


data = input().split()
n, m = map(int, data)
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
dist = bf(n, edges, source=1)
INF = 30000
print(" ".join([str(d if d < INF else INF) for d in dist]))