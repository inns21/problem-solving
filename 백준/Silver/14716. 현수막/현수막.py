from collections import deque

m,n = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
    
def bfs(a,b, visited):
    q = deque([(a,b)])
    visited[a][b] = True
    
    while q:
        x,y = q.popleft()
        for nx,ny in [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
            dx, dy = x + nx, y + ny
            if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy] and graph[dx][dy] == 1:
                visited[dx][dy] = True
                q.append((dx,dy))
                
                
visited = [[False]*n for i in range(m)]
result = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i,j,visited)
            result += 1
            
print(result)
    
    