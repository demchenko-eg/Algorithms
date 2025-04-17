n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    l = 2 * i + 1
    if l < n and a[i] > a[l]:
        print("NO")
        exit()
    r = 2 * i + 2
    if r < n and a[i] > a[r]:
        print("NO")
        exit()
print("YES")