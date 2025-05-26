import heapq

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))
visited = [False] * (n + 1)
mh = [(0, 1)]
total = 0
while mh:
    weiht, u = heapq.heappop(mh)
    if visited[u]:
        continue
    visited[u] = True
    total += weiht
    for w, v in G[u]:
        if not visited[v]:
            heapq.heappush(mh, (w, v))
print(total)