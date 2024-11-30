def find(parent, x):
  if parent[x] != x:
      parent[x] = find(parent, parent[x])  
  return parent[x]

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a > b:
      parent[a] = b
  else:
      parent[b] = a

g = int(input()) 
p = int(input()) 

parent = list(range(g + 1)) 
count = 0

for _ in range(p):
  gate = int(input())
  docking = find(parent, gate)  
  if docking == 0: 
      break
  union(parent, docking, docking - 1)
  count += 1

print(count)
