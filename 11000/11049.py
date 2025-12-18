import sys

input = sys.stdin.readline

N = int(input())

# P는 0부터 N
for i in range(N):
    if i==0:
        P = list(map(int,input().split()))
    else:
        u,v = map(int, input().split())
        P.append(v)

M = [[0]*(N+1) for _ in range(N+1)]

for L in range(2,N+1):
    for i in range(1,N+2-L, 1):
        j = i+L-1
        M[i][j]=sys.maxsize
        for k in range(i,j,1):
            M[i][j]=min(M[i][j], M[i][k] + M[k+1][j] + P[i-1]*P[k]*P[j])
            
print(M[1][N])