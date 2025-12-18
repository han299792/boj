import sys, heapq

input = sys.stdin.readline

N  = int(input())
p = []
for _ in range(N):
    u, v = map(int, input().split())
    p.append((u,v))

p.sort(key=lambda x:(x[1], x[0]))
endpoint=0
cnt = 0
for i in range(N):
    if p[i][0] >= endpoint:
        endpoint=p[i][1]
        cnt += 1
    
print(cnt)

