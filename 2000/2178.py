import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*M for _ in range(N)] 
visited[0][0] = True
dist = [[0]*N for _ in range(N)]

queue = deque([(0,0)])

while queue:
    (x,y) = queue.popleft()
    
    if x == N-1 and y == M-1:
        print(dist[x][y] +1)
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny <M:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] +1
                
            
    
    