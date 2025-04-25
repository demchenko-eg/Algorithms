n, m = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(m)]
s = set(A)
cout = n * (n - 1) // 2
print("YES" if len(s) == cout else "NO")