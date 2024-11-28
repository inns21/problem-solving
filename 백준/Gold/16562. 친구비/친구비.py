n, m, k = map(int, input().split())  # 학생 수, 친구 관계 수, 예산
pay = list(map(int, input().split()))  # 각 학생의 친구비

parent = [i for i in range(n+1)]  # Union-Find 초기화

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        # 더 작은 번호가 루트가 되도록 합침
        if root_a > root_b:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a

# 친구 관계 입력
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

# 각 학생이 속한 그룹별로 친구비 저장
group_costs = {}
for i in range(1, n+1):
    root = find(i)
    if root not in group_costs:
        group_costs[root] = []
    group_costs[root].append(pay[i-1])  # pay 배열은 0-based, student는 1-based

# 각 그룹의 최소 친구비를 계산
min_costs = [min(costs) for costs in group_costs.values()]
total_cost = sum(min_costs)

# 예산 내에 해결 가능한지 체크
if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")
