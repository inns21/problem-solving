n = int(input())
k = int(input())

cards = []
for i in range(n):
  cards.append(input())

def pick(current, card, k, results):
  if len(current) == k:
      results.add(''.join(current))
      return

  for i in range(len(card)):
      pick(current + [card[i]], card[:i] + card[i+1:], k, results)


result = set()
pick([], cards, k, result)

print(len(result))
