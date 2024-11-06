from collections import deque

m, n, h = map(int, input().split())

mn_list = [[] for i in range(h)]
for i in range(h):
    for j in range(n):
        mn_list[i].append(list(map(int, input().split())))

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

def bfs():
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if mn_list[i][j][k] == 1:
                    q.append((i, j, k))
                    visited[i][j][k] = True

    while q:
        z, x, y = q.popleft()
        for dz, dx, dy in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if not visited[nz][nx][ny] and mn_list[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = True
                    mn_list[nz][nx][ny] = mn_list[z][x][y] + 1
                    q.append((nz, nx, ny))

    max_days = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if mn_list[i][j][k] == 0: 
                    return -1
                max_days = max(max_days, mn_list[i][j][k])

    return max_days-1

print(bfs())
