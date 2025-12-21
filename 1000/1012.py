import sys
from collections import deque

input = sys.stdin.readline

def solve():
    M, N, K = map(int, input().split())
    
    graph = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    
    for _ in range(K):
        u, v = map(int, input().split())
        graph[u][v] = 1
        
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    cnt = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
 
                        if 0 <= nx < M and 0 <= ny < N:
                            if graph[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
    print(cnt)

T = int(input())
for _ in range(T):
    solve()