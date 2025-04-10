from collections import deque

a,b,n,m = map(int,input().split())
visted = [False for _ in range(100001)]
def bfs(x):
  q = deque([(x,0)])
  visted[x] = True
  while q:
    v,dist = q.popleft()
    for i in [1,-1,a,-a,b,-b,v*a-v,v*b-v]:
      nv = v + i
      if nv == m:
        return dist+1

      if 0 <= nv <= 100000 and not visted[nv]:
        visted[nv] = True
        q.append((nv, dist+1))
  return dist
print(bfs(n))

