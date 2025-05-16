n = int(input())
g = [input() for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
vis = [[0] * n for _ in range(n)]
stack = [(r, c)]
vis[r][c] = 1
ans = 0
while stack:
    x, y = stack.pop()
    ans += 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and g[nx][ny] == '.':
            vis[nx][ny] = 1
            stack.append((nx, ny))
print(ans)