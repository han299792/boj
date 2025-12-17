import sys 
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0,0)])

visited = [[False]*M for _ in range(N)]
visited[0][0] = True

dist = [[0]*M for _ in range(N)]

while queue:
    v = queue.popleft()
    (a, b) = v

    if a == (N-1) and b == (M-1):
        print(dist[a][b]+1)
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and not visited[nx][ny]:            
                queue.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[a][b] + 1

            