import sys

T = int(sys.stdin.readline().strip())

# 각 숫자의 마지막 자리수 반복 패턴을 미리 저장
patterns = {
    0: [10],  # 10으로 처리
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    
    # a의 마지막 자리수
    last_digit = a % 10
    
    # 패턴을 이용해 결과를 찾기
    cycle = patterns[last_digit]
    index = (b - 1) % len(cycle)  # 패턴의 길이를 이용해 인덱스 찾기
    
    print(cycle[index])
