import sys
from collections import deque

# 입력 속도 빠르게
input = sys.stdin.readline

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

# N: 정점 개수, M: 간선 개수, V: 시작 정점
N, M, V = map(int, input().split())

# 인덱스 편하게 하려고 N+1만큼 생성
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향이니까 반대도 추가

# 작은 번호부터 방문해야 하니까 정렬 (이 문제 핵심!)
for i in range(1, N + 1):
    graph[i].sort()

# DFS 실행
visited_dfs = [False] * (N + 1)
dfs(V)
print() # 줄바꿈

# BFS 실행
visited_bfs = [False] * (N + 1)
bfs(V)