import sys

data = sys.stdin.read().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
M = int(data[3])

stress = 0 
work = 0 

for _ in range(24):
    if stress + A <= M:
        work += B
        stress += A
    else:
        stress = max(0, stress - C)

print(work)