from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def kin():
    N = int(input())
    A, B = map(int,input().split())
    M = int(input())
    
    graph = defaultdict(list)
    
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * (N+ 1)
    q = deque([(A, 0)])
    visited[A] = True
    
    while q:
        current_node, degree = q.popleft()
        
        if current_node == B:
            return degree
        
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, degree+1))
                
    return -1

print(kin())
        
        