import heapq

def dfhjl(a ,b):
    return sum(x != y for x, y in zip(a, b))

n, k = map(int, input().split())
S = [input().strip() for _ in range(n)]
visited = [False] * n
mh = [(0, 0, -1)]
total = 0
edg = []
while mh and len(edg) < n - 1:
    weht, u, par = heapq.heappop(mh)
    if visited[u]:
        continue
    visited[u] = True
    if par != -1:
        edg.append((par, u))
        total += weht
    for v in range(n):
        if not visited[v]:
            dist = dfhjl(S[u], S[v])
            heapq.heappush(mh, (dist, v, u))
print(total)
for u, v in edg:
    print(u, v)