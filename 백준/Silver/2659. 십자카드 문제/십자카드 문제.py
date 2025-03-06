from collections import deque

def get_clock_num(num):
    return min(int(str(num)[i:] + str(num)[:i]) for i in range(4))

nums = deque(map(int, input().split()))
min_num = get_clock_num(int(''.join(map(str, nums))))

result = 0
for x in range(1111, min_num + 1):
    if '0' not in str(x) and get_clock_num(x) == x:
        result += 1

print(result)
