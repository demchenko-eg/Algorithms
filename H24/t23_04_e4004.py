def dfs(u):
    V[u] = 1
    for v in range(n):
        if A[u][v]:
            if V[u] == 1:
                return True
            if V[v] == 0 and dfs(v):
                return True
    V[u] = 2
    return False

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
V = [0] * n
for i in range(n):
    if V[i] and dfs(i):
        print(1)
        break
else:
    print(0)