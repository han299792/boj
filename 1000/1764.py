import sys

data = sys.stdin.read().split()
N, M = int(data[0]), int(data[1])

A = data[2:N+2]
B = data[N+2:]
C = list(set(A)&set(B))
C.sort()

print(len(C))
for i in range(len(C)):
    print(C[i])