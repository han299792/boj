def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

def union(parent, a, b):
    a, b = parent(parent, a), parent(parnet, b )
    if a < b:
        parent[b] = a
        