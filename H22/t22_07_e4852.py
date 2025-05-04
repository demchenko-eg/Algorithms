def BFS(graph, start):
    visited = [False] * len(graph)
    dist = [-1] * len(graph)
    queue = [start]
    head = 0
    visited[start] = True
    dist[start] = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in range(len(graph)):
            if graph[u][v] == 1 and not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

n, x = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
d = BFS(graph, x-1)
print(*d)