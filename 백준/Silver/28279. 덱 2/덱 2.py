from collections import deque
import sys

n = int(input())

result = deque()
for i in range(n):
  prompt = list(map(int,sys.stdin.readline().split()))
  if prompt[0] == 1:
    result.appendleft(prompt[1])
  elif prompt[0] == 2:
    result.append(prompt[1])
  elif prompt[0] == 3:
    if not result:
      print(-1)
    else:
      print(result.popleft())
  elif prompt[0] == 4:
    if not result:
      print(-1)
    else:
      print(result.pop())
  elif prompt[0] == 5:
    print(len(result))
  elif prompt[0] == 6:
    if not result:
      print(1)
    else:
      print(0)
  elif prompt[0] == 7:
    if not result:
      print(-1)
    else:
      print(result[0])
  elif prompt[0] == 8:
    if not result:
      print(-1)
    else:
      print(result[-1])


  