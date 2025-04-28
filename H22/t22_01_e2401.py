def BFS(graph, start):
    queue = [start]
    d = [-1] * len(graph)
    d[start] = 0
    head = 0
    while head < len(queue):
        curr = queue[head]
        head +=1
        for k in graph[curr]:
            if d[k] == -1:
                d[k] = d[curr] + 1
                queue.append(k)
    return d


n, s, f = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
G = {i: [] for i in  range(n)}
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            G[i].append(j)
s -= 1
f -= 1

D = BFS(G, s)
if D[f] == -1:
    print(0)
else:
    print(D[f])