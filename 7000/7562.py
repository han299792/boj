import sys
from collections import deque

input = sys.stdin.readline

def solve():
    I = int(input())
    iu, iv = map(int, input().split())
    fu, fv = map(int, input().split())
    
    if iu == fu and iv == fv:
        return 0

    visited = [[-1] * I for _ in range(I)]
    
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    
    queue = deque([(iu, iv)])
    visited[iu][iv] = 0
    
    while queue:
        x, y = queue.popleft()

        if x == fu and y == fv:
            return visited[x][y]
            
        for k in range(8):  
            nx, ny = x + dx[k], y + dy[k]
            
            if 0 <= nx < I and 0 <= ny < I:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

T = int(input())
for _ in range(T):
    print(solve())