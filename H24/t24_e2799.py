from collections import deque

def f1(n, m, s1, s2, A):

    s1 -= 1
    s2 -= 1
    ds = [(-1, 0, 2, 8), (1, 0, 8, 2), (0, -1, 1, 4), (0, 1, 4, 1)]
    q = deque()
    v = [[[False]*2 for _ in range(m)] for _ in range(n)]
    q.append((s1, s2, 0, 0))
    v[s1][s2][0] = True
    while q:
        x, y, gold, count = q.popleft()
        cell = A[x][y]
        if (x == 0 and not (cell & 2)) or (x == n-1 and not (cell & 8)) or (y == 0 and not (cell & 1)) or (y == m-1 and not (cell & 4)):
            if gold:
                return count
        if cell & 16:
            gold = 1
        for dx, dy, ws, w in ds:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not (cell & ws) and not (A[nx][ny] & w):
                    if not v[nx][ny][gold]:
                        v[nx][ny][gold] = True
                        q.append((nx, ny, gold, count + 1))
    return -1

n, m, si, sj = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(f1(n, m, si, sj, A))