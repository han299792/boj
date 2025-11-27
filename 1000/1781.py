import sys
import heapq
 
n = int(sys.stdin.readline())
prob = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    prob.append((a, b))
    
prob.sort()
heap = []

for a, b in prob:
    heapq.heappush(heap, b)
    if len(heap) > a:
        heapq.heappop(heap)
    
print(sum(heap))
        
