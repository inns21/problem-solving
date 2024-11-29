import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  
        size[root_x] += size[root_y] 


T = int(input().strip())

for _ in range(T):
    f = int(input().strip())
    parent = {}
    size = {}

    for _ in range(f):
        a, b = input().strip().split()

        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1

        union(parent, size, a, b)
        print(size[find(parent, a)])
