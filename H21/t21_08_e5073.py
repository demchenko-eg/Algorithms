n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
s = set()
flag = False
for u, v in A:
    if (u, v) in s:
        flag = True
        break
    s.add((u, v))
print("YES" if flag else "NO")