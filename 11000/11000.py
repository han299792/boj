# 힙 = 현재 사용중인 강의실들 / 힙의 최소값=가장 빨리 비는 강의실

import sys, heapq
input = sys.stdin.readline

N=int(input())
P=[]
for _ in range(N):
    s,t = map(int, input().split())
    P.append((s,t))
    
P.sort(key=lambda x:x[0])
pri_q=[]

for s,t in P:
    if pri_q and pri_q[0] <= s:
        heapq.heappop(pri_q)
    heapq.heappush(pri_q, t)
    
print(len(pri_q))