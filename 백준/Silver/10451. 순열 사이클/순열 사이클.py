from collections import deque

T = int(input())

def dfs(s):
  q = deque([s])
  visited[s] = True
  while q:
    x = q.popleft()
    if not visited[arr_dict[x]]:
      q.append(arr_dict[x])
      visited[arr_dict[x]] = True

for i in range(T):
  n = int(input())
  arr = list(map(int, input().split()))
  arr_dict = {i+1:arr[i] for i in range(n)}
  visited = [False] * (n+1)
  result = 0
  for j in range(1,n+1):
    if not visited[j]:
      dfs(j)
      result += 1
  print(result)