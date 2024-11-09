from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = {i + 1: list() for i in range(n)}
kg = []
for i in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
  kg.append(c)

return_x, return_y = map(int, input().split())

start = 1
end = max(kg)
result = 0
while start <= end:
  mid = (start + end) // 2

  q = deque([return_x])
  visited = [False for i in range(n + 1)]
  visited[return_x] = True
  find = False
  while q:
    x = q.popleft()

    for y, z in graph[x]:
      if not visited[y] and z >= mid:
        if y == return_y:
          find = True
          break
        q.append(y)
        visited[y] = True

    if find:
      break
  if find:
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)
