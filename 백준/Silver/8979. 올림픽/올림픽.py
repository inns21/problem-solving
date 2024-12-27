n, k = map(int, input().split())
countries = []

for _ in range(n):
    countries.append(list(map(int, input().split())))

# 금, 은, 동 메달 수 기준으로 내림차순 정렬
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 순위 계산
ranks = [0] * n  # 각 국가의 순위를 저장할 리스트
rank = 1  # 현재 순위
ranks[countries[0][0] - 1] = rank  # 첫 번째 국가의 순위

for i in range(1, n):
    if countries[i][1:] == countries[i - 1][1:]:  # 메달 수가 같으면 동일 순위
        ranks[countries[i][0] - 1] = rank
    else:
        rank = i + 1  # 메달 수가 다르면 현재 인덱스 + 1로 순위 갱신
        ranks[countries[i][0] - 1] = rank

print(ranks[k - 1])
