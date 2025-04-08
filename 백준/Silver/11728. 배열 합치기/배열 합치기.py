a, b = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
i, j = 0, 0
for _ in range(a + b):
    if A[i] > B[j]:
        result.append(B[j])
        j += 1
    elif A[i] < B[j]:
        result.append(A[i])
        i += 1
    elif A[i] == B[j]:
        result.append(A[i])
        result.append(B[j])
        i += 1
        j += 1
    if i == a:
        result.extend(B[j:])
        break
    elif j == b:
        result.extend(A[i:])
        break
print(*result)
