from collections import deque

n,k = map(int, input().split())

def bfs(s):
  q = deque([s])
  visited = [False] * 100001
  visited[s] = True
  while q:
    x = q.popleft()
    if x == k:
      return visited[x]
    for nx in (x-1, x+1, x*2):
      if 0 <= nx <= 100000 and not visited[nx]:
        visited[nx] = visited[x] + 1
        q.append(nx)

print(bfs(n)-1)
