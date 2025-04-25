n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            print(i+1, j+1)