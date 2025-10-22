import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])
C = int(data[2])

D = str(A*B*C)
for j in range(10):
    cnt = 0
    for i in range(len(D)):
        if D[i] == str(j):
            cnt += 1
    print(cnt)