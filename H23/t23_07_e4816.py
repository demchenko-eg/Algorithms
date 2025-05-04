def read():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, graph

n, graph = read()
visited = [False] * (n + 1)
components = []
for i in range(1, n + 1):
    if not visited[i]:
        stack = [i]
        comp = []
        visited[i] = True
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        components.append(comp)
print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)