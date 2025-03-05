from collections import deque

a,b = map(int,input().split())

q = deque([(a,0)])
while q:
    x, cnt = q.popleft()
    if x == b:
        print(cnt+1)
        break
    for i in [2*x,x*10+1]:
        if 0 <= i <= b:
            q.append((i,cnt+1))
else:
  print(-1)
