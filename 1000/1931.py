import sys
data = sys.stdin.read().split()
N = int(data[0])
A = []
cnt = 0 
for i in range(1,2*N+1, 2):
    A.append((int(data[i]), int(data[i+1])))

A.sort(key=lambda x:(x[1], x[0]))
endpoint = 0


for i in range(N):
    if A[i][0] >= endpoint:
        cnt += 1
        endpoint = A[i][1]

print(cnt)

