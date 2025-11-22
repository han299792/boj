V= int(input())
E = int(input())
edges = [[] for  _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    
def dfs(x):
    stack = [x]
    visited[x] = True
    cnt = 0 
    while stack:
        node = stack.pop()
        for next_node in edges[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
                cnt += 1
    return cnt

visited = [False for _ in range(V+1)]
print(dfs(1))