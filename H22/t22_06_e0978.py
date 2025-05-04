def BFS(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    head = 0
    tree_edges = []
    visited[start] = True
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                tree_edges.append((u, v))
                queue.append(v)
    return tree_edges

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

tree = BFS(graph, 1)
for u, v in tree:
    print(u, v)