import sys
input = sys.stdin.readline

text = list(input().rstrip())
m = int(input().rstrip())

# 왼쪽 스택과 오른쪽 스택
left_stack = text
right_stack = []

for _ in range(m):
    command = input().split()

    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':  # 커서 왼쪽 문자 삭제
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':  # 커서 왼쪽에 문자 삽입
        left_stack.append(command[1])

print(''.join(left_stack + right_stack[::-1]))
