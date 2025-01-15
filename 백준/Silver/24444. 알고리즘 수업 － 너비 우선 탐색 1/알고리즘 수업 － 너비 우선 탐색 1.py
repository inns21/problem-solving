import sys
from collections import deque

input = sys.stdin.readline

# 정점 수, 간선 수, 시작 정점 입력
n, m, r = map(int, input().split())

# 그래프 초기화
graph = {i+1: [] for i in range(n)}

# 간선 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정렬을 한 번에 처리
for key in graph:
    graph[key].sort()

# BFS 구현
def bfs(start):
    result = [0] * (n+1)  # 방문 순서 저장
    visited = [False] * (n+1)  # 방문 여부 저장
    cnt = 1  # 방문 순서 카운트

    visited[start] = True
    result[start] = cnt
    q = deque([start])

    while q:
        x = q.popleft()
        for neighbor in graph[x]:
            if not visited[neighbor]:
                cnt += 1
                visited[neighbor] = True
                result[neighbor] = cnt
                q.append(neighbor)

    return result

# BFS 실행 및 결과 출력
result = bfs(r)
print("\n".join(map(str, result[1:])))
