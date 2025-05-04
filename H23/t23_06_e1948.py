def read():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1
    return n, graph, indegree

def tsort(n, graph, indegree):
    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    result = []
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    if len(result) == n:
        print(*result)
    else:
        print(-1)


n, graph, indegree = read()
tsort(n, graph, indegree)