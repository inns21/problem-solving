n = int(input())

for _ in range(n):
    text = list(input())
    left_stack = []
    right_stack = []
    
    for i in range(len(text)):
        if text[i] == '<':  # 커서를 왼쪽으로 이동
            if left_stack:
                right_stack.append(left_stack.pop())
        elif text[i] == '>':  # 커서를 오른쪽으로 이동
            if right_stack:
                left_stack.append(right_stack.pop())
        elif text[i] == '-':  # 커서 왼쪽 문자 삭제
            if left_stack:
                left_stack.pop()
        else:  # 커서 왼쪽에 문자 삽입
            left_stack.append(text[i])
    
    print(''.join(left_stack + right_stack[::-1]))
    