n = int(input())
A = [[0] * n for _ in range(n)]
for i in range(n):
    d = list(map(int, input().split()))
    k = d[0]
    if k > 0:
        for j in d[1:]:
            A[i][j-1] = 1
for r in A:
    print(*r)