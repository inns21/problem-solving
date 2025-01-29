def find_tree(buildings, depth):
  if not buildings:
      return

  mid = len(buildings) // 2
  result[depth].append(buildings[mid])

  find_tree(buildings[:mid], depth + 1)
  find_tree(buildings[mid+1:], depth + 1)

k = int(input())
buildings = list(map(int, input().split()))
result = [[] for _ in range(k)]

find_tree(buildings, 0)

for i in result:
  print(*i)
