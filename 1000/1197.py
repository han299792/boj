import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))   # (to, weight)
    graph[v].append((u, w))

visited = [False] * (V + 1)
pq = [(0, 1)]                 # (weight, node)
mst_cost = 0
picked = 0

while pq and picked < V:
    w, u = heapq.heappop(pq)  # (weight, node) 순서로 받아야 함
    if visited[u]:
        continue
    visited[u] = True
    mst_cost += w
    picked += 1

    for v, nw in graph[u]:
        if not visited[v]:
            heapq.heappush(pq, (nw, v))  # (weight, node)

print(mst_cost)
