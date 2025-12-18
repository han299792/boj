import sys
input = sys.stdin.readline

N = int(input())
P = []
max_d = 0

for _ in range(N):
    d, w = map(int, input().split())  
    P.append((d, w))
    if d > max_d:
        max_d = d

P.sort(key=lambda x: (-x[1], x[0]))

Ans = [0] * (max_d + 1)

for d, w in P:
    for day in range(d, 0, -1):
        if Ans[day] == 0:
            Ans[day] = w
            break

print(sum(Ans))
