import sys 
import heapq

data = sys.stdin.read().split()

T = int(data[0])
P = list(map(int, data[1:]))
l = []
for p in P:
    if p==0:
        if not l:
            print("0")
        else:
            print(heapq.heappop(l))
    else:
        heapq.heappush(l, p)  

