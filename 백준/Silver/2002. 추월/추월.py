n = int(input())

in_c = {}
out_c = {}

for i in range(n):
    car = input()
    in_c[car] = i

for i in range(n):
    car = input()
    out_c[car] = i

count = 0
out_keys = list(out_c.keys())

for i in range(0, n-1):
    now = in_c[out_keys[i]]
    for j in range(i+1, n):
        next_in = in_c[out_keys[j]]
        if next_in < now:
            count += 1
            break

print(count)
