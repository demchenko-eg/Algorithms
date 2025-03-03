def f(current, used, n, k):
    if len(current) == k:
        print(" ".join(str(num) for num in current))
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            current.append(i)
            f(current, used, n, k)
            current.pop()
            used[i] = False

n, k = map(int, input().split())
used = [False] * (n + 1)
f([], used, n, k)