import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int, input().split())
graph = [[] for i in range(n+1)]


for i in range(m):
    a,b,d = map(int, input().split())
    graph[a].append((b,d))
    

def dijkstra(start,distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


result_list = [[0*(n+1)]]
for i in range(n):
    distance = [INF] * (n+1)
    result_list.append(dijkstra(i+1,distance))    
    
result = []
for i in range(1,n+1):
    dist = result_list[i][x] + result_list[x][i]
    result.append(dist)

print(max(result))