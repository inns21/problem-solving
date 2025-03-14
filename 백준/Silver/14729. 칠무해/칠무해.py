n = int(input())
n_list = list()

for i in range(n):
    n_list.append(float(input()))
n_list.sort()
for i in range(7):
    print(f'{n_list[i]:.3f}')