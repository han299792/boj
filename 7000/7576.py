import sys
from collections import deque

def solve():
    input = sys.stdin.readline

    M, N = map(int, input().split(' '))
    graph = [list(map(int, input().split(' '))) for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]

    queue = deque()
    max_data = 0

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j))
                visited[i][j] = 0
                
    while queue:
        (x, y) = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < N and 0<= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
            
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return "-1"
            max_data = max(max_data, visited[i][j])
            
    return max_data

print(solve())