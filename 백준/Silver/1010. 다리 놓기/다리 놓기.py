T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    result = 1

    for i in range(m, m-n, -1):
        result *= i

    for i in range(1, n+1):
        result //= i

    print(result)
