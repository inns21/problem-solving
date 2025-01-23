import sys

s, e, q = sys.stdin.readline().split()

def time_to_int(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

s = time_to_int(s)
e = time_to_int(e)
q = time_to_int(q)

attended = set()
counted = set()
cnt = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        time, name = line.split()
        time = time_to_int(time)
        
        if time <= s:
            attended.add(name)
        elif e <= time <= q and name in attended and name not in counted:
            cnt += 1
            counted.add(name)
    except ValueError:
        continue

print(cnt)
