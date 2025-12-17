import sys 
from collections import deque
input = sys.stdin.readline

N= int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = []
visited = [[False]*N for _ in range(N)]
num = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]==1:
            queue = deque([(i,j)])
            visited[i][j] = True
            cnt = 1 
            num += 1  
            while queue:
                v = queue.popleft()
                (a, b) = v
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] == 1 and not visited[nx][ny]:            
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            cnt += 1
            ans.append(cnt)
print(num)                    
ans.sort()
for _ in range(len(ans)):
    print(ans[_])