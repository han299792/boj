from collections import defaultdict
import heapq
import sys 

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
in_degree = [0]*(N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v]+=1

queue = []
    
for i in range(1, N+1):
    if in_degree[i]==0:
        heapq.heappush(queue, i)

result = []
        
while queue:
    v = heapq.heappop(queue)
    result.append(v)
    
    for i in graph[v]:
        in_degree[i]-=1
        if in_degree[i]==0:
            heapq.heappush(queue, i)
        
print(*(result))