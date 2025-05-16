def bfs(grid, start, end):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]
    si, sj = start
    visited[si][sj] = True
    queue = [(si, sj)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        i, j = queue.pop(0)
        if (i, j) == end:
            break
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if grid[ni][nj] == '.' or grid[ni][nj] == 'X':
                    visited[ni][nj] = True
                    parent[ni][nj] = (i, j)
                    queue.append((ni, nj))
    return visited, parent

def f1(parent, start, end):
    path = []
    current = end
    while current is not None and current != start:
        path.append(current)
        current = parent[current[0]][current[1]]
    if current == start:
        path.append(start)
        path.reverse()
        return path
    return []

def f2(grid, path):
    for i, j in path:
        if grid[i][j] == '.':
            grid[i][j] = '+'


n = int(input())
grid = [list(input().strip()) for _ in range(n)]
start = end = None
for i in range(n):
    for j in range(n):
        if grid[i][j] == '@':
            start = (i, j)
        if grid[i][j] == 'X':
            end = (i, j)
visited, parent = bfs(grid, start, end)
if not visited[end[0]][end[1]]:
    print('N')
else:
    print('Y')
    path = f1(parent, start, end)
    f2(grid, path)
    for row in grid:
        print(''.join(row))