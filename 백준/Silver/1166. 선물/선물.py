N,L,W,H = map(int, input().split())

start = 0
end = min(L,W,H)

cuboid = L*W*H

for i in range(100):
  mid = (start + end) / 2

  if (L // mid) * (W // mid) * (H // mid) >= N:
    start = mid
  else:
    end = mid
print(f"{mid:.9f}")