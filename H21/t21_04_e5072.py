n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
c = 0
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            c += 1
print(c)