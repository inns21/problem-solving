import heapq

INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
  distance = [INF] * (N + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, node = heapq.heappop(q)

    if dist > distance[node]:
      continue

    for next_node, weight in graph[node]:
      new_dist = dist + weight
      if new_dist < distance[next_node]:
        distance[next_node] = new_dist
        heapq.heappush(q, (new_dist, next_node))

  return distance


s_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

r1 = s_dist[v1] + v1_dist[v2] + v2_dist[N]
r2 = s_dist[v2] + v2_dist[v1] + v1_dist[N]

answer = min(r1,r2)
if answer >= INF:
  print(-1)
else:
  print(answer)