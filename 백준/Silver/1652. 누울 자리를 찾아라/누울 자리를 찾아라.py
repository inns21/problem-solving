n = int(input())

w_graph = [list(input().strip()) for i in range(n)]

l = 0
w = 0

for i in range(n):
  cnt = 0
  for j in range(n):
    if w_graph[i][j] == '.':
      cnt += 1
    if w_graph[i][j] == 'X':
      if cnt >= 2:
        w += 1
      cnt = 0
  if cnt >= 2:
    w += 1
    

l_graph = [[] for i in range(n)]
for i in range(n):
  for j in range(n):
    l_graph[j].append(w_graph[i][j])
     
for i in range(n):
  cnt = 0
  for j in range(n):
    if l_graph[i][j] == '.':
      cnt += 1
    if l_graph[i][j] == 'X':
      if cnt >= 2:
        l += 1
      cnt = 0
  if cnt >= 2:
    l += 1

      
print(w,l)