def f(index, score, time, used, missions, n, k, min_time):
    if score >= k:
        return min(min_time, time)
    for i in range (n):
        if not used[i]:
            used[i] = True
            min_time = f(index, score + missions[i][0], time + missions[i][1], used, missions, n, k, min_time)
            used[i] = False
    return min_time

n, k = map(int, input().split())
missions = [tuple(map(int, input().split())) for _ in range(n)]
used = [False] * n
r = f(0, 0, 0, used, missions, n, k, float('inf'))
print(r if r != float('inf') else -1)