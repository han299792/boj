import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split(' '))) for _ in range(N)]

visited = [[False]*M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            queue = deque([(i,j)])
            visited[i][j] = True
            cnt = 1
    
            while queue:
                (x, y) = queue.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if 0<= nx < N and 0<= ny < M:
                        if graph[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            cnt += 1

            ans.append(cnt)

print(len(ans))
if len(ans) > 0:
    print(max(ans))
else:
    print(0)