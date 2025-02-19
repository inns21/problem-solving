import sys
from collections import deque

def dfs(a,b):
  q = deque([(a,b)])
  visited[a][b] = True
  while q:
    x,y = q.popleft()
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
      nx,ny = x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and graph[nx][ny] == 1:
        visited[nx][ny] = True
        q.append((nx,ny))


while True:
  w,h = map(int, sys.stdin.readline().split())
  if w == 0 and h == 0:
    break
  else:
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
      for j in range(w):
        if graph[i][j] == 1 and not visited[i][j]:
          cnt += 1
          dfs(i, j)
    print(cnt)
    
  