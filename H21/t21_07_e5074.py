n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
d = [0] * n
for u, v in A:
    d[u - 1] += 1
    d[v - 1] += 1
for d in d:
    print(d)