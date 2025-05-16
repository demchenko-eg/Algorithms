def read():
    h, m, n = map(int, input().split())
    levels = []
    for _ in range(h):
        level = [list(input().rstrip()) for _ in range(m)]
        levels.append(level)
        if _ != h-1:
            input()
        return h, m, n, levels

def f(h, m, n, levels):
    q = [(0, 0, 0, 0)]
    v = [[[False for _ in range(n)] for _ in range(m)] for _ in range(h)]
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if levels[z][x][y] == '1':
                    q[0] = (z, x, y, 0)
                    v[z][x][y] = True
                if levels[z][x][y] == '2':
                    pass




from collections import deque

def f1(n, m, si, sj, grid):

    si -= 1
    sj -= 1
    directions = [(-1, 0, 2, 8), (1, 0, 8, 2), (0, -1, 1, 4), (0, 1, 4, 1)]
    queue = deque()
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
    queue.append((si, sj, 0, 0))
    visited[si][sj][0] = True
    while queue:
        x, y, has_gold, steps = queue.popleft()
        cell = grid[x][y]
        if (x == 0 and not (cell & 2)) or (x == n-1 and not (cell & 8)) or (y == 0 and not (cell & 1)) or (y == m-1 and not (cell & 4)):
            if has_gold:
                return steps
        if cell & 16:
            has_gold = 1
        for dx, dy, wall_mask, opposite_wall in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not (cell & wall_mask) and not (grid[nx][ny] & opposite_wall):
                    if not visited[nx][ny][has_gold]:
                        visited[nx][ny][has_gold] = True
                        queue.append((nx, ny, has_gold, steps + 1))
    return -1

n, m, si, sj = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(f1(n, m, si, sj, grid))


