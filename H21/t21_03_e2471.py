class Graph:
    def __init__(self, vertex_number):
        self.adj = [[] for _ in range(vertex_number + 1)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def vertex(self, u):
        return self.adj[u]


n = int(input())
k = int(input())
g = Graph(n)
for _ in range(k):
    parts = input().split()
    if parts[0] == '1':
        u, v = int(parts[1]), int(parts[2])
        g.addEdge(u, v)
    else:
        u = int(parts[1])
        neighbors = g.vertex(u)
        if neighbors:
            print(*neighbors)
        else:
            print() 