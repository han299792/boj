import sys
data = sys.stdin.read().split()

N  = int(data[0])

cal = [0] * (N + 1)
cal[1] = 0
if N >= 2:
    cal[2] = 1
if N >= 3:
    cal[3] = 1

for i in range(4, N+1):
    min_cal = cal[i-1] + 1
    if i%2 == 0:
        min_cal = min(cal[i//2]+1, min_cal)
    if i%3 == 0:
        min_cal = min(cal[i//3]+1, min_cal)
    cal[i] = min_cal
print(cal[N])