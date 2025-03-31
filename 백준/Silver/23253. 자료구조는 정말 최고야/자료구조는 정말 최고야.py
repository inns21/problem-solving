import sys

n, m = map(int, sys.stdin.readline().split())
possible = True

stacks = []
for _ in range(m):
    k = int(sys.stdin.readline())
    stack = list(map(int, sys.stdin.readline().split()))
    stacks.append(stack)

for stack in stacks:
  for i in range(len(stack)-1):
    if stack[i] < stack[i+1]:
        possible = False
        break
  if not possible:
      break

print("Yes" if possible else "No")