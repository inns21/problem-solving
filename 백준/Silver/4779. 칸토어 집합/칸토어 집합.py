import sys
input = sys.stdin.read

def cantor(n, start, end):
    if n == 0:
        return ['-'] * (end - start)

    length = end - start
    third = length // 3
    result = cantor(n - 1, start, start + third)
    result += [' '] * third
    result += cantor(n - 1, start + 2 * third, end)
    return result

data = input().strip().split()
for line in data:
    n = int(line)
    size = 3 ** n
    result = cantor(n, 0, size)
    print(''.join(result))
