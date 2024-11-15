import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for i in range(T):
  p = input().strip()
  n = int(input())
  s = input().strip()
  if p.count('D') > n:
    print('error')
    continue
  set_s = deque(s[1:len(s) - 1].split(','))
  reversed = False
  for j in p:
    if j == 'R':
      if reversed:
        reversed = False
      else:
        reversed = True
    elif j == 'D':
      if reversed:
        set_s.pop()
      else:
        set_s.popleft()
  if reversed:
    set_s.reverse()
  print('[' + ','.join(set_s) + ']')
