def read():
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n):
        parts = list(map(int, input().split()))
        for v in parts[1:]:
            graph[v - 1].append(i)
    return n, graph

def dfs(graph, start, n):
    visited = [False] * n
    stack = [start]
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    stack.append(v)
    return all(visited)


n, original = read()
if n == 2:
    print(0)
    exit()
for pivot in range(n):
    graph = [[] for _ in range(n)]
    for u in range(n):
        for v in original[u]:
            if u == pivot:
                graph[v].append(u)
            elif v == pivot:
                graph[pivot].append(u)
            else:
                graph[u].append(v)
    if dfs(graph, pivot, n):
        print(1)
        exit()
print(0)