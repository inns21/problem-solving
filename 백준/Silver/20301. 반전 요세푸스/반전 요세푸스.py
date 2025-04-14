from collections import deque

n,k,m = map(int, input().split())
n_list = deque([i+1 for i in range(n)])


count = 0
r = True
while n_list:
  if count == m:
    if r:
      r = False
    else:
      r = True
    count = 0
  if r:
    n_list.rotate(-(k-1))
    print(n_list.popleft())
    count += 1
  else:
    n_list.rotate(k)
    print(n_list.popleft())
    count += 1