import sys

data = sys.stdin.read().split()

N, K = int(data[0]), int(data[1])
A = list(map(int, data[2:]))

cnt = 0

while K > 0:
    for i in range(N-1, -1, -1):
       if A[i] <= K:
            cnt += K//A[i]
            K = K%A[i]

print(cnt)