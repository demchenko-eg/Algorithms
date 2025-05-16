def f1():
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]
    start1 = start2 = exit_pos = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '1':
                start1 = (i, j)
                grid[i][j] = '.'
            elif grid[i][j] == '2':
                start2 = (i, j)
                grid[i][j] = '.'
            elif grid[i][j] == '*':
                exit_pos = (i, j)
                grid[i][j] = '.'
    return H, W, grid, start1, start2, exit_pos

def bfs_(H, W, grid, start1, start2, exit_pos):
    dirs = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]
    start = (*start1, *start2)
    goal = (*exit_pos, *exit_pos)
    queue = [start]
    visited = {start: None}
    head = 0
    while head < len(queue):
        y1, x1, y2, x2 = queue[head]
        head += 1
        if (y1, x1, y2, x2) == goal:
            return visited, True
        for cmd, dy, dx in dirs:
            ny1, nx1 = f3(y1, x1, dy, dx, H, W, grid)
            ny2, nx2 = f3(y2, x2, dy, dx, H, W, grid)
            new_state = (ny1, nx1, ny2, nx2)
            if new_state not in visited:
                visited[new_state] = ((y1, x1, y2, x2), cmd)
                queue.append(new_state)
    return visited, False

def f3(y, x, dy, dx, H, W, grid):
    ny, nx = y + dy, x + dx
    if not (0 <= ny < H and 0 <= nx < W) or grid[ny][nx] == '#':
        return y, x
    return ny, nx

def f2(visited, exit_pos):
    goal = (*exit_pos, *exit_pos)
    if goal not in visited:
        return None
    path = []
    cur = goal
    while visited[cur] is not None:
        prev, cmd = visited[cur]
        path.append(cmd)
        cur = prev
    return path[::-1]


H, W, grid, s1, s2, exit_p = f1()
visited, found = bfs_(H, W, grid, s1, s2, exit_p)
if not found:
    print(-1)
    exit()
path = f2(visited, exit_p)
print(len(path))
print(''.join(path))