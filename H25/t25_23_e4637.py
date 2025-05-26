def bf2(grid, K):
    M, N = len(grid), len(grid[0])
    INF = float('-inf')
    best = [[INF] * N for _ in range(M)]
    cnt = [[[0] * (K + 1) for _ in range(N)] for _ in range(M)]
    best[0][0] = grid[0][0]
    cnt[0][0][0] = 1
    for i in range(M):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            cs = []
            if i > 0:
                cs.append((best[i-1][j], cnt[i-1][j]))
            if j > 0:
                cs.append((best[i][j-1], cnt[i][j-1]))
            max_pred = max(p for p, _ in cs)
            best[i][j] = max_pred + grid[i][j]
            for best_p, cnt_p in cs:
                offset = max_pred - best_p
                for d in range(K + 1):
                    if cnt_p[d] == 0:
                        continue
                    d_new = offset + d
                    if d_new <= K:
                        cnt[i][j][d_new] += cnt_p[d]
    ms = best[M-1][N-1]
    tp = sum(cnt[M-1][N-1][d] for d in range(K + 1))
    return ms, tp


M, N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
ms, goood = bf2(grid, K)
print(ms)
print(goood)