from collections import deque

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))


visited = [[False]*n for i in range(n)]
def bfs(graph, visited, a, b):
    q = deque([(a,b)])
    visited[a][b] = True

    home_length = 1
    while q:
      x,y = q.popleft()
      for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
            home_length += 1
            visited[nx][ny] = True
            q.append((nx,ny))
    return  home_length

cnt = 0
size_list = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            home_count = bfs(graph, visited, i, j)
            size_list.append(home_count)
            cnt += 1
print(cnt)
for i in sorted(size_list):
    print(i)

