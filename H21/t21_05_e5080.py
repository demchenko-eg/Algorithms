n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    d = sum(m[i])
    if d == 1:
        count += 1
print(count)