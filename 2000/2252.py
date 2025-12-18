import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    graph=defaultdict(list)
    in_degree = [0]*(1+N)
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    queue = deque()
    for i in range(1,N+1):
        if in_degree[i]==0:
            queue.append(i)
            
    cnt = 0
    top_order=[]
    while queue:
        v = queue.popleft()
        top_order.append(v)
        
        for i in graph[v]:
            in_degree[i] -= 1
            if in_degree[i]==0:
                queue.append(i)
        
        cnt += 1
    
    print(*(top_order)) 
        
    
                
    return 

solve()