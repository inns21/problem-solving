scores = {}

for i in range(8):
  scores[i+1] = int(input())

scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print(sum([x[1] for x in scores[:5]]))
print(*[x[0] for x in sorted(scores[:5])])