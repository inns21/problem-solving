r,c,n = map(int, input().split())

graph = []
for i in range(r):
  graph.append(input().strip())

if n % 2 == 0:
  result = [['O']*c for i in range(r)]
  for i in result:
    print(''.join(i))
else:
  for i in range(n//2):
    result = [['O']*c for i in range(r)]
    for j in range(r):
      for k in range(c):
        if graph[j][k] == 'O':
          result[j][k] = '.'
          for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
            dx,dy = j+x, k+y
            if 0 <= dx < r and 0 <= dy < c:
                result[dx][dy] = '.'  
    graph = result
  for i in graph:
    print(''.join(i))