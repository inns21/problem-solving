import sys

n = int(input())
n_list = []

for i in range(n):
  n_list.append(sys.stdin.readline().rstrip())

k = 1
for i in range(1, len(n_list[0])+1):
  checked = set()
  for j in n_list:
    checked.add(j[-i:])
  if len(checked) == n:
    k = i
    break

print(k)
