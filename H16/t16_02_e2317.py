def lca(a, b, parent, depth):
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

k = int(input().strip())
parent = {1: None}
depth = {1: 0}
for _ in range(k):
    parts = input().strip().split()
    if parts[0] == "ADD":
        a = int(parts[1])
        b = int(parts[2])
        parent[b] = a
        depth[b] = depth[a] + 1
    elif parts[0] == "GET":
        a = int(parts[1])
        b = int(parts[2])
        print(lca(a, b, parent, depth))