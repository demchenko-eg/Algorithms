def rec(i, mask, n):
    if i == n:
        return 0
    if (i, mask) in dp:
        return dp[(i, mask)]
    best = float('inf')
    for j in range(n):
        if mask & (1 << j) == 0:
            new_mask = mask | (1 << j)
            candidate = cost[i][j] + rec(i + 1, new_mask, n)
            best = min(best, candidate)
    dp[(i, mask)] = best
    return best

n = int(input().strip())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = {}
print(rec(0, 0, n))