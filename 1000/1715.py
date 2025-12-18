import sys, heapq

data = sys.stdin.readline

N = int(input())
P = []
for _ in range(N):
    P.append(int(input().strip()))

heapq.heapify(P)
result = 0
while len(P)>1:
    a, b = heapq.heappop(P), heapq.heappop(P)
    c = a+b
    result += c
    heapq.heappush(P, c)
    
print(result)