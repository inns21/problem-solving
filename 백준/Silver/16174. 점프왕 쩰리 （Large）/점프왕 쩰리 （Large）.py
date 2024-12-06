from collections import deque

n = int(input())

def bfs(graph, visited):
  q = deque([(0,0)])
  visited[0][0] = True
  while q:
    x,y = q.popleft()
    length = graph[x][y]
    for dx,dy in [(0,length),(length,0)]:
      nx,ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if graph[nx][ny] == -1:
          visited[nx][ny] = True
          break
        visited[nx][ny] = True
        q.append((nx,ny))

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
visited = [[False]*n for i in range(n)]

bfs(graph, visited)
if not visited[n-1][n-1]:
  print('Hing')
else:
  print('HaruHaru')