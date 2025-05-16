def dfs(grid, i, j, visited):
    m = len(grid)
    n = len(grid[0])
    stack = [(i, j)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        ci, cj = stack.pop()
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < m and 0 <= nj < n:
                if not visited[ni][nj] and grid[ni][nj] == '#':
                    visited[ni][nj] = True
                    stack.append((ni, nj))

def f1(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False] * n for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                visited[i][j] = True
                dfs(grid, i, j, visited)
                count += 1
    return count


m, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(m)]
print(f1(grid))