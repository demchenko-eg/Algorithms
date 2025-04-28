def BFS(graph, start):
    queue = [start]
    d = {i: -1 for i in graph}
    p = {i: -1 for i in graph}
    d[start] = 0
    head = 0
    while head < len(queue):
        curr = queue[head]
        head += 1
        for k in graph[curr]:
            if d[k] == -1:
                d[k] = d[curr] + 1
                p[k] = curr
                queue.append(k)
    return d, p


n, m = map(int, input().split())
a, b = map(int, input().split())
G = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dist, par = BFS(G, a)

if dist[b] == -1:
    print(-1)
else:
    path = []
    c = b
    while c != -1:
        path.append(c)
        c = par[c]
    path.reverse()
    print(len(path) - 1)
    print(*path)