from collections import deque
from re import X

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)

for i in range(n+1):
  graph[i].sort()

visited = [False]*(n+1)
def bfs(start):
  distance = [-1] * (n + 1)
  distance[start] = 0
  q = deque([start])

  while q:
      x = q.popleft()
      for i in graph[x]:
          if distance[i] == -1: 
              distance[i] = distance[x] + 1
              q.append(i)

  return [i for i in range(1, n + 1) if distance[i] == k]

result = bfs(x)

print('\n'.join(map(str, result)) if len(result) != 0 else -1)