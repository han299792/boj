import sys, heapq
input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    row = map(int, input().split())
    for x in row:
        if len(h) < N:
            heapq.heappush(h, x)
        else:
            if x > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, x)

print(h[0])
