import sys
import heapq

data = sys.stdin.read().split()
T = int(data[0])
P = list(map(int, data[1:]))

h = []
for x in P:
    if x == 0:
        if not h:
            print(0)
        else:
            print(-heapq.heappop(h))    # 다시 부호 복원 -> 최대값
    else:
        heapq.heappush(h, -x)           # 부호 반전해서 push
