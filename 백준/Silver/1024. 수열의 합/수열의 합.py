def find_sequence(N, L):
    for length in range(L, 101):
        temp = N - (length * (length - 1)) // 2
        if temp < 0: 
            break
        if temp % length == 0: 
            x = temp // length
            if x >= 0:
                return [x + i for i in range(length)]
    return -1 


N, L = map(int, input().split())
result = find_sequence(N, L)


if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))
