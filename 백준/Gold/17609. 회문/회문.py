import sys

n = int(sys.stdin.readline())

for i in range(n):
    result = 0
    word = sys.stdin.readline().strip()
    start = 0
    end = len(word) - 1
    oneChance = True

    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            if oneChance:
                # 양쪽 문자를 각각 제거하여 부분 문자열이 회문인지 확인
                check_start = word[start+1:end+1]  # 왼쪽 문자 제거
                check_end = word[start:end]  # 오른쪽 문자 제거
                
                if check_start == check_start[::-1] or check_end == check_end[::-1]:
                    result = 1  # 유사회문
                else:
                    result = 2  # 전혀 회문 아님
                oneChance = False
                break
            else:
                result = 2
                break

    print(result)
