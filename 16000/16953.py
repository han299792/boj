import sys
data = sys.stdin.read().split()
A, B = int(data[0]), int(data[1])

a = []
cnt = 0
while B > A:
    if B%2 == 0:
        cnt += 1
        B = B//2
    else:
        if B%10 != 1:
            break
        else:
            B = B//10
            cnt += 1
    
if B == A:
    print(cnt+1)
else:
    print("-1")    