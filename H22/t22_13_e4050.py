def f(n, k, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    queue = [k]
    head = 0
    parent[k] = -1
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                children[u].append(v)
                queue.append(v)

    g = [0] * (n + 1)
    for u in reversed(queue):
        s = {g[c] for c in children[u]}
        mex = 0
        while mex in s:
            mex += 1
        g[u] = mex

    if g[k] == 0:
        return False, None

    for v in sorted(children[k]):
        if g[v] == 0:
            return True, v


n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
win, airport = f(n, k, edges)
if not win:
    print("First player loses")
else:
    print("First player wins flying to airport", airport)