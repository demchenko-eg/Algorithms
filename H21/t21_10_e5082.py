n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
f = []
for i in range(n):
    d = sum(A[i])
    f.append(d)
print(*f)