import sys
from PriorityQueue import PriorityQueue

INF = sys.maxsize
GR = None
N = 0

def init(vertices, edges):
    global GR, N
    N = vertices
    GR = [[] for _ in range(vertices)]

def addEdge(source, destination, weight):
    global GR
    GR[source].append((destination, weight))

def getWay(start, end):
    dist = [INF] * N
    prev = [-1] * N
    dist[start] = 0
    pq = PriorityQueue()
    pq.insert(start, 0)
    while not pq.empty():
        u = pq.extractMinimum()
        if u == end:
            break
        for v, w in GR[u]:
            new_d = dist[u] + w
            if new_d < dist[v]:
                dist[v] = new_d
                prev[v] = u
                if v in pq:
                    pq.updatePriority(v, new_d)
                else:
                    pq.insert(v, new_d)
    if dist[end] == INF:
        return []
    path = []
    v = end
    while v != -1:
        path.append(v)
        v = prev[v]
    path.reverse()
    return path