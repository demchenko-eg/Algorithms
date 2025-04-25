n, m = map(int, input().split())
A = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    A[a-1][b-1] = 1
for r in A:
    print(*r)