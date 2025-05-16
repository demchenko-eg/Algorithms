import heapq

GR = None
N = 0

def init(vertices, edges):
    global GR, N
    N = vertices
    GR = [[] for _ in range(vertices)]

def addEdge(source, destination, weight):
    global GR
    GR[source].append((destination, weight))

def findDistance(start, end):
    global GR, N
    INF = float('inf')
    dist = [INF] * N
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == end:
            return d
        for v, w in GR[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return -1 if dist[end] == INF else dist[end]