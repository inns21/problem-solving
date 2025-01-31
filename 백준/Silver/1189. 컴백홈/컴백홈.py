r, c, k = map(int, input().split())

graph = []
for i in range(r):
    graph.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    if x == 0 and y == c-1:
        return 1 if cnt == k else 0

    result = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == '.':
            visited[nx][ny] = True
            result += dfs(nx, ny, cnt + 1)
            visited[nx][ny] = False

    return result

visited = [[False]*c for i in range(r)]
visited[r-1][0] = True  
print(dfs(r-1, 0, 1))
