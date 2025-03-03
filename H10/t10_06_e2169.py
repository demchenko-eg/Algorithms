def f(current, used, n):
    if len(current) == n:
        print(" ".join(str(num) for num in current))
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            current.append(i)
            f(current, used, n)
            current.pop()
            used[i] = False

n = int(input().strip())
used = [False] * (n + 1)
f([], used, n)