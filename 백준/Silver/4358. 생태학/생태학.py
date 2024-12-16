import sys

trees = {}
total = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break

    total += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

trees = sorted(trees.items(),key=lambda x : x[0])
for k,v in trees:
  print(f'{k} {v/total*100:.4f}')


