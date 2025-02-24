def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a

a,b = map(int, input().split(":"))
r = Euclidean(a, b)

print(f'{a//r}:{b//r}')