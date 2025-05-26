import heapq

def de(n, adj, s, f):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    visited = [False] * (n + 1)
    heap = [(0, s)]
    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if u == f:
            break
        for v in range(1, n + 1):
            w = adj[u][v]
            if w >= 0 and not visited[v]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
    return dist[f] if dist[f] != INF else -1


n, s, f = map(int, input().split())
A = [[-1] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j, w in enumerate(row, start=1):
        A[i][j] = w
print(de(n, A, s, f))