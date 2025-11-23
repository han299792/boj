import sys
input = sys.stdin.readline
N, M = map(int, input().split())
D = {}
for _ in range(N):
    a= input().split()
    D[a[0]]=a[1]

for _ in range(M):
    para = input().rstrip() # 은 리스트를 만들어서 안됨
    print(D[para])    