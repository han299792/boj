import sys
data = sys.stdin.read().split()

E, S, M = map(int, data)
E = E - 1 
S = S - 1
M = M - 1

for i in range (0, 100000, 28):
    y1 = i + S
    if (y1%19 - M == 0) and (y1%15 - E == 0) :
        break

print(y1 + 1)
    